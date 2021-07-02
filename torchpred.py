import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
from PIL import Image
import cv2


def torchpreduh(temp):
    temp=str(temp)
    device=torch.device('cpu')
    model=torch.load("model.pth", map_location=torch.device('cpu'))
    for param in model.parameters():
        param.requires_grad = False
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 2)
    model = model.to(device)

    model=model.eval()


    transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], 
                             [0.229, 0.224, 0.225]),])

    
    image =transform(Image.open(temp))
    image=image.unsqueeze(0)
    image=image.to(device)
    outputs = model(image).to(device)
    _, predicted = torch.max(outputs, 1)
    index = predicted.argmax().item()

    if(predicted[0]==torch.tensor(0)):
        #print(predicted[0])
        return 0
    elif(predicted[0]==torch.tensor(1)):
        #print(predicted[0])
        return 1
