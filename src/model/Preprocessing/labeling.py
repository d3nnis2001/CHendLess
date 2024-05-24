import torch
from torchvision import models, transforms
from PIL import Image
import requests
import cv2
from sklearn.cluster import KMeans
import webcolors

# ResNet
model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
model.eval()

# Size the image correctly
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def load_image(image_path):
    input_image = Image.open(image_path).convert("RGB")
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)
    return input_batch


def load_imagenet_classes():
    response = requests.get("https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt")
    return response.text.split("\n")


# Get labels with highest probabilities (greater than 0.5)
def label_image(image_path):
    input_batch = load_image(image_path)

    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')

    with torch.no_grad():
        output = model(input_batch)

    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    probs, ids = torch.topk(probabilities, 5)
    imagenet_classes = load_imagenet_classes()

    labels = []
    for i in range(probs.size(0)):
        if probs[i].item() > 0.5:
            labels.append((imagenet_classes[ids[i]], probs[i].item()))

    return labels

# Gets the closest colour from a colour code
def closest_color(color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - color[0]) ** 2
        gd = (g_c - color[1]) ** 2
        bd = (b_c - color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

# Uses clustering to get the 2 most common colours in a picture
def get_dominant_colors(image_path, k=2):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    kmeans = KMeans(n_clusters=k)
    kmeans.fit(image)
    colors = kmeans.cluster_centers_

    dominant_colors = []
    for color in colors:
        dominant_colors.append(closest_color(color))

    return dominant_colors


if __name__ == "__main__":
    # TODO: Add connection where it runs for every image before storing inside db
    image_path = "GET IMAGE HERE"
    classification_labels = label_image(image_path)
    dominant_colors = get_dominant_colors(image_path)

    print("Classification Labels:")
    print(classification_labels)
    print("Dominant Colors:")
    print(dominant_colors)
