#%%
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
import matplotlib.pyplot as plt
from pathlib import Path
print(torch.__version__)
print(torchvision.__version__)