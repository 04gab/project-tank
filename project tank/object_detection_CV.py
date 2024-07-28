#%%
import torch 
from torch import nn
print(torch.__version__)
# computer vision
# ----------------------------------------------------------------------------------------------------------
# %%
model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
model
# %%
