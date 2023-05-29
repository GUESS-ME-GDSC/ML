from torch.utils.data import Dataset
import numpy as np
from PIL import Image
import torch
import PIL.ImageOps


class SiameseNetworkDataset(Dataset):
    def __init__(self, image1_path, image2_path, transform=None, should_invert=True):
        self.image1_path = image1_path
        self.image2_path = image2_path
        self.transform = transform
        self.should_invert = should_invert

    def __getitem__(self, _):
        img0 = Image.open(self.image1_path)
        img1 = Image.open(self.image2_path)
        img0 = img0.convert("L")
        img1 = img1.convert("L")

        if self.should_invert:
            img0 = PIL.ImageOps.invert(img0)
            img1 = PIL.ImageOps.invert(img1)

        if self.transform is not None:
            img0 = self.transform(img0)
            img1 = self.transform(img1)

        return img0, img1, torch.from_numpy(np.array([1], dtype=np.float32))

    def __len__(self):
        return 1
