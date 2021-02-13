import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models
from utils import accuracy


class PneumoniaClassificationBase(nn.Module):
    def training_step(self, batch):
        images, targets = batch
        out = self(images)
        loss = F.cross_entropy(out, targets)
        return loss

    def validation_step(self, batch):
        images, targets = batch
        out = self(images)                    # Generate predictions
        loss = F.cross_entropy(out, targets)  # Calculate loss
        acc = accuracy(out, targets)

        return {'val_loss': loss.detach(), 'val_acc': acc}

    def validation_epoch_end(self, outputs):
        batch_losses = [x['val_loss'] for x in outputs]
        epoch_loss = torch.stack(batch_losses).mean()  # Combine loss
        batch_acc = [x['val_acc'] for x in outputs]
        epoch_acc = torch.stack(batch_acc).mean()       # Combine accuracies

        return {'val_loss': epoch_loss.item(), 'val_score': epoch_acc.item()}

    def epoch_end(self, epoch, result):
        print("Epoch [{}], last_lr: {:.4f}, train_loss: {:.4f}, val_loss: {:.4f}, val_score: {:.4f}".format(
            epoch, result['lrs'][-1], result['train_loss'], result['val_loss'], result['val_score']))


class PneumoniaResnet(PneumoniaClassificationBase):
    def __init__(self):
        super().__init__()

        # Use a pretrained model
        self.network = models.resnet34(pretrained=True)

        # Replace last layer
        num_ftrs = self.network.fc.in_features
        self.network.fc = nn.Dropout(0.5)
        self.network.fc = nn.Linear(num_ftrs, 2)
    
    def forward(self, xb):
        return self.network(xb)
    
    def freeze(self):
        # To freeze the residual layers
        for param in self.network.parameters():
            param.requires_grad = True