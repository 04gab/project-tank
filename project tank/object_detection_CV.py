#%%
import torch 
from torch import nn
import cv2
print(torch.__version__)
print(cv2.__version__)
# computer vision
# ----------------------------------------------------------------------------------------------------------
# %%
model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
model
# %%
