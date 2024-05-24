import requests
from pymongo import MongoClient, errors
from bson.binary import Binary
from PIL import Image
from io import BytesIO

keys = ['Name', 'Price', 'Amount sold', 'Image', 'Product Link']

def resize_and_save_image(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((128, 128))
    byte_arr = BytesIO()
    image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()

    image_data = Binary(byte_arr)
    return image_data

# The function assumes that the arrays have the same length. Please run this ONLY once this has been ensured
def store_page(entries, category_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AliExpress']
    collection = db[category_name]

    documents = []
    for entry in entries:
        document = {}
        for i in range(len(entry)):
            if keys[i] == 'Image':
                # Resize and save the image, then store the new image path in the document
                document[keys[i]] = resize_and_save_image(entry[i])
            else:
                document[keys[i]] = entry[i]
        documents.append(document)

    # Insert into DB; catch any duplicates
    #try:
    collection.insert_many(documents, ordered=False)
    #except errors.BulkWriteError as e:
        #write_errors = e.details['writeErrors']
        #for error in write_errors:
            #if error['code'] == 11000:  # Duplicate key error code
                #print(f"INFO: Duplicate entry found in category \"{category_name}\" for Product Link: {error['op']['Product Link']}")

    print("DONE saving to Database!")

def check_duplicates(category_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AliExpress']
    collection = db[category_name]

    # Aggregate to find duplicates in 'Product Link'
    pipeline = [
        {"$group": {"_id": "$Product Link", "count": {"$sum": 1}}},
        {"$match": {"count": {"$gt": 1}}}
    ]

    duplicates = collection.aggregate(pipeline)

    # Print duplicates
    for duplicate in duplicates:
        print(duplicate)