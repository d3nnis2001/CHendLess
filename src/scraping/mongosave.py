import requests
from pymongo import MongoClient
from bson.binary import Binary
from PIL import Image
from io import BytesIO
from Preprocessing.labeling import label_image, get_dominant_colors
from Preprocessing.removeBackground import getOptimizedImage
import base64

keys = ['Name', 'Price', 'Amount sold', 'Image', 'Product Link', 'Labeling']

def resize_and_save_image(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((128, 128))
    byte_arr = BytesIO()
    image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()

    return base64.b64encode(byte_arr).decode('utf-8')


def getLabeling(image_base64):
    classification_labels = label_image(image_base64)
    dominant_colors = get_dominant_colors(image_base64)
    return classification_labels, dominant_colors


def store_page(entries, category_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AliExpress']
    collection = db[category_name]

    documents = []
    last_Img = ""
    for entry in entries:
        document = {}
        for i in range(len(keys)):
            if i == len(keys) - 1:  # Handling the last element for labeling
                if last_Img:
                    labeling = getLabeling(last_Img)
                    document[keys[i]] = f"Resnet: {labeling[0]}, Colours: {labeling[1]}"
                else:
                    document[keys[i]] = "No image available"
            elif keys[i] == 'Image':
                if entry[i]:
                    resized_image_base64 = resize_and_save_image(entry[i])
                    document[keys[i]] = resized_image_base64
                    last_Img = resized_image_base64
                else:
                    document[keys[i]] = None
            else:
                document[keys[i]] = entry[i]
        documents.append(document)

    collection.insert_many(documents, ordered=False)
    print("DONE saving to Database!")


def check_duplicates(category_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AliExpress']
    collection = db[category_name]

    # Aggregate to find duplicates in 'Product Link'
    pipeline = [
        {"$group": {"_id": "$Product Link", "dups": {"$push": "$_id"}, "count": {"$sum": 1}}},
        {"$match": {"count": {"$gt": 1}}}
    ]

    duplicates = collection.aggregate(pipeline)

    # Print and remove duplicates
    for duplicate in duplicates:
        for id in duplicate['dups'][1:]:
            collection.delete_one({'_id': id})
