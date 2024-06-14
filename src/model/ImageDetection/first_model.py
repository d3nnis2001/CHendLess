import os
import cv2
import numpy as np
from PIL import Image
from pymongo import MongoClient
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
import base64
from io import BytesIO

# Initialisiere das VGG16-Modell
base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

def extract(img):
    """
    Extrahiert Features aus einem Bild mithilfe des VGG16-Modells.
    """
    img = img.resize((224, 224))
    img = img.convert('RGB')
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    feature = model.predict(x)[0]
    return feature / np.linalg.norm(feature)

def read_all_documents(category_name):
    """
    Liest alle Dokumente aus einer MongoDB-Kollektion.
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AliExpress']
    collection = db[category_name]

    documents = collection.find()
    return list(documents)

def decode_image(image_base64):
    """
    Dekodiert ein base64-kodiertes Bild.
    """
    image_data = base64.b64decode(image_base64)
    image = Image.open(BytesIO(image_data))
    return image

def find_closest_images(category_name, query_image_path):
    """
    Findet die fünf ähnlichsten Bilder zu einem Abfragebild.
    """
    documents = read_all_documents(category_name)
    all_features = np.zeros(shape=(len(documents), 4096))
    images = []

    for i, doc in enumerate(documents):
        img_data_base64 = doc.get('Image')
        if img_data_base64:
            img = decode_image(img_data_base64)
            feature = extract(img)
            all_features[i] = np.array(feature)
            images.append(doc.get('Name', f'Image_{i}'))
        else:
            all_features[i] = np.zeros(4096)
            images.append(f'Missing_Image_{i}')

    query = extract(img=Image.open(query_image_path))
    dists = np.linalg.norm(all_features - query, axis=1)
    ids = np.argsort(dists)[:5]

    return [images[i] for i in ids]

category_name = "example_category"
query_image_path = "image_to_match.png"

closest_images = find_closest_images(category_name, query_image_path)

print("The closest matched images are:", closest_images)
