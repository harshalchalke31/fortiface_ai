from torch.utils.data import DataLoader, Dataset, random_split
from torchvision import transforms
from PIL import Image
import glob
import os
import torch


class ImageDataset(Dataset):
    def __init__(self, anc_path,pos_path,neg_path,transform=None):
        self.anchor_images=glob.glob(os.path.join(anc_path,'*.jpg'))[:500]
        self.positive_images=glob.glob(os.path.join(pos_path,'*.jpg'))[:500]
        self.negative_images=glob.glob(os.path.join(neg_path,'*.jpg'))[:500]
        self.transform=transform

        # combine positives and negatives with labels
        self.data=[]
        self.labels=[]

        for anc,pos in zip(self.anchor_images,self.positive_images):
            self.data.append((anc,pos))
            self.labels.append(1)
        
        for anc,neg in zip(self.anchor_images,self.negative_images):
            self.data.append((anc,neg))
            self.labels.append(0)
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        anchor_path, pair_path = self.data(index)
        label=self.labels(index)

        anchor_img = Image.open(anchor_path).convert("RGB")
        pair_img = Image.open(pair_path).convert("RGB")

        if self.transform:
            anchor_img=self.transform(anchor_img)
            pair_img=self.transform(pair_img)
        
        return anchor_img, pair_img, torch.tensor(label,dtype=torch.float32)