from pymongo import MongoClient
import base64
import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from rembg import remove
import cv2

client = MongoClient('mongodb://localhost:27017/')
db = client['AliExpress']

# Gets all products from a collection
def getAllProducts(collection):
    collection = db[collection]
    documents = collection.find()
    all_documents = list(documents)
    return all_documents

# Extracted Base64 to image
def getAllImagesFromBase64(allProducts):
    images_base64 = []
    for product in allProducts:
        if 'Image' in product:
            image_base64 = product['Image']
            if isinstance(image_base64, str):
                missing_padding = len(image_base64) % 4
                if missing_padding:
                    image_base64 += '=' * (4 - missing_padding)
            images_base64.append(image_base64)
    return images_base64

# Plots image for debugging
def displayImage(image):
    plt.figure()
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# Removes noise from an image
def removeNoise(image):
    open_cv_image = np.array(image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    denoised_image = cv2.GaussianBlur(open_cv_image, (5, 5), 10)
    return denoised_image

# Apply threshold to remove unwanted parts
def applyThreshold(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresholded_image = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)[1]
    return thresholded_image

# Combine the original image with the thresholded mask
def applyMask(original_image, mask):
    masked_image = cv2.bitwise_and(original_image, original_image, mask=mask)
    return masked_image

# Removes background using rembg (very nice libary)
def removeBackground(image_base64):
    try:
        print(f"Opening image with PIL")
        image = Image.open(BytesIO(image_base64))
        output_image = remove(image)
        return output_image
    except Exception as e:
        print(f"Fehler beim Verarbeiten des Bildes: {e}")
        return None


def main():
    allProducts = getAllProducts("Spielzeugpistolen")
    images_base64 = getAllImagesFromBase64(allProducts)
    for i in range(10):
        withoutBack = removeBackground(images_base64[i])
        if withoutBack:
            denoised_image = removeNoise(withoutBack)
            thresholded_image = applyThreshold(denoised_image)
            masked_image = applyMask(np.array(withoutBack), np.array(thresholded_image))
            displayImage(masked_image)

if __name__ == "__main__":
    main()
