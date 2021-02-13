import torch
from torch.optim import optimizer
from model import PneumoniaResnet

@torch.no_grad()
def evaluate(model, val_loader):
    model.eval()
    outputs = [model.PneumoniaResnet.validation_step(batch) for batch in val_loader]
    return model.validation_epoch_end(outputs)