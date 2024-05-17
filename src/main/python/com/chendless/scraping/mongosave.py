import requests
from pymongo import MongoClient
from bson.binary import Binary
from PIL import Image
from io import BytesIO

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
def store_page(sold, name, price, image_urls):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AliExpress']
    collection = db['Test']

    for i in range(len(sold)):

        document = {
            'Name': name[i],
            'Price': price[i],
            'Amount sold': sold[i],
            'Image': resize_and_save_image(image_urls[i])
        }
        collection.insert_one(document)
