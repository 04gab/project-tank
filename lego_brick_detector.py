#%%
import kagglehub
import os
import cv2

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
# %%
