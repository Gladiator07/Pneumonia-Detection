import torch
from torch.utils.data import Dataset, random_split, DataLoader
from PIL import Image
import torchvision.models as models
import torchvision.transforms as T

# Importing local modules
from data_prep import prepare_data
import config


class PneumoniaDataset(Dataset):
    def __init__(self, df, transform=None):
        self.df = df
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.loc[idx]
        img_fname, img_label = row['image'], row['label']
        img = Image.open(img_fname)
        if self.transform:
            img = self.transform(img)
        if img.shape[0] == 1:
            img = img.repeat(3, 1, 1)

# Defining some transforms


train_transform = T.Compose([T.Resize((256, 256)),
                             T.RandomAffine(30)],
                            T.ColorJitter(),
                            T.ToTensor())

val_transform = T.Compose([T.Resize(256, 256),
                           T.ToTensor()])

train_df, val_df = prepare_data()

train_dataset = PneumoniaDataset(train_df, transform=train_transform)
val_dataset = PneumoniaDataset(val_df, transform=val_transform)


# PyTorch Data Loaders
# train_dl = DataLoader(tra)
