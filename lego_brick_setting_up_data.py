#%%
import kagglehub
import os
import cv2
import numpy as np
import torch 
from torch import nn
import torch.utils
import torch.utils.data
import torchvision
from torchvision import datasets
from torchvision import transforms
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
from timeit import default_timer as timer
import requests
from tqdm.auto import tqdm
import matplotlib.pyplot as plt
from pathlib import Path
print(torch.__version__)
print(torchvision.__version__)
#%%
# Download latest version
path = kagglehub.dataset_download("joosthazelzet/lego-brick-images")

print("Path to dataset files:", path)

image_folder = 'C:/Users/04gab/Documents/GitHub/project-tank/2x2 brick images'  # Change this path to your folder of images
if not os.path.exists(image_folder):
    print(f"Directory does not exist: {image_folder}")
else:
    print(f"Directory exists: {image_folder}")
#%%
# Check if the directory exists
if os.path.exists(image_folder):
    # List all items in the directory
    all_files = os.listdir(image_folder)
    print(f"Total items in the folder: {len(all_files)}")

    # Filter for only image files
    image_files = [f for f in all_files if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    print(f"Number of image files: {len(image_files)}")

else:
    print(f"Directory does not exist: {image_folder}")
#%%
# Get the first file in the directory
first_file = None
for filename in os.listdir(image_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # Specify your image formats
        first_file = os.path.join(image_folder, filename)
        break  # Stop after finding the first image

# Print the first image path
print(first_file)

# %%
import torch
import torchvision.transforms as T
from torchvision import transforms
from torchvision.models import detection
from PIL import Image

# Load the image
image_path = first_file  # use the path of your first image

image = Image.open(first_file).convert("RGB")  # Ensure the image is in RGB format

# Print the image to verify it's loaded
print("Image loaded:", image)

# Transform the image
transform = T.Compose([
    T.Resize((800, 800)),  # Resize the image
    T.ToTensor(),          # Convert image to tensor
])

# Transform the image
transform = transforms.Compose([
    transforms.ToTensor(),  # Convert the image to a tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize
])

image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

# Print the shape of the tensor
print("Tensor shape:", image_tensor.shape)
#%%
# Load the pre-trained model
model = detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()  # Set the model to evaluation mode

# Get predictions
with torch.no_grad():  # Disable gradient calculation
    predictions = model(image_tensor)

# Extract bounding boxes and labels
boxes = predictions[0]['boxes']
labels = predictions[0]['labels']
scores = predictions[0]['scores']

# Display the results (e.g., print boxes and labels)
for box, label, score in zip(boxes, labels, scores):
    if score > 0.5:  # Only display boxes with a score above 0.5
        print(f'Box: {box}, Label: {label}, Score: {score}')

# %%
import matplotlib.pyplot as plt

# Convert the image to numpy array for plotting
image_np = np.array(image)

# Plot the image
plt.imshow(image_np)
for box, label, score in zip(boxes, labels, scores):
    if score > 0.5:
        x_min, y_min, x_max, y_max = box
        plt.gca().add_patch(plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, fill=False, color='red', linewidth=2))
        plt.text(x_min, y_min, f'Label: {label}, Score: {score:.2f}', fontsize=12, color='white', bbox=dict(facecolor='red', alpha=0.5))

plt.axis('off')
plt.show()
# %%
import matplotlib.pyplot as plt

def update_box(event):
    # Logic to update the bounding box based on user input
    pass

fig, ax = plt.subplots()
plt.imshow(image_np)

# Display bounding boxes
for box in boxes:
    rect = plt.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], fill=False, color='red')
    ax.add_patch(rect)

plt.show()