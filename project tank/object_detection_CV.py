#%%
import torch
import torchvision
import os
from os import listdir
print(torch.__version__)
print(torchvision.__version__)
# computer vision
# ----------------------------------------------------------------------------------------------------------
#%%
print(os.listdir())
folder_dir = "1"
i=0
for images in os.listdir(folder_dir):
    if images.endswith(".png"):
        print(f"image number {i}")
        i+=1
# %%
