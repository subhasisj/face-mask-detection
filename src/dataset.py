import albumentations as A
import torch
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from torch.utils.data import Dataset

# custom dataset class for albumentations library
class AlbumentationImageDataset(Dataset):
    def __init__(self, image_list):
        self.image_list = image_list

        self.aug = A.Compose({
        A.Resize(224),
        # A.CenterCrop(100, 100),
        # A.RandomCrop(80, 80),
        A.HorizontalFlip(p=0.5),
        A.Rotate(limit=(-90, 90)),
        A.VerticalFlip(p=0.5),
        A.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
        })
        
    def __len__(self):
        return (len(self.image_list))

    def __getitem__(self, i):
        image = plt.imread(self.image_list[i])
        image = Image.fromarray(image).convert('RGB')
        image = self.aug(image=np.array(image))['image']
        image = np.transpose(image, (2, 0, 1)).astype(np.float32)
        
        return torch.tensor(image, dtype=torch.float)