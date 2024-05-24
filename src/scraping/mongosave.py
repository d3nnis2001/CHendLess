import requests
from pymongo import MongoClient
from bson.binary import Binary
from PIL import Image
from io import BytesIO
from Preprocessing.labeling import label_image, get_dominant_colors
from Preprocessing.removeBackground import (getOptimizedImage)

keys = ['Name', 'Price', 'Amount sold', 'Image', 'Product Link']

def resize_and_save_image(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((128, 128))
    byte_arr = BytesIO()
    image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()

    image_data = Binary(byte_arr)
    optImg = getOptimizedImage(image_data)
    opt_data = Binary(optImg)
    return opt_data

def getLabeling(image):
    classification_labels = label_image(image)
    dominant_colors = get_dominant_colors(image)
    return classification_labels, dominant_colors

# The function assumes that the arrays have the same length. Please run this ONLY once this has been ensured
def store_page(entries, category_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AliExpress']
    collection = db[category_name]

    documents = []
    last_Img = ""
    for entry in entries:
        document = {}
        for i in range(len(entry)+1):
            if i == len(entry):
                labeling = getLabeling(last_Img)
                document[keys[i]] = f"Resnet: {labeling[0]}, Colours: {labeling[1]}"
            if keys[i] == 'Image':
                # Resize and save the image, then store the new image path in the document
                document[keys[i]] = resize_and_save_image(entry[i])
                last_Img = document[keys[i]]
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
        # Skip the first item from the dups list
        for id in duplicate['dups'][1:]:
            collection.delete_one({'_id': id})