from src.biggan import BigGAN128
from src.biggan import BigGAN256 
from src.biggan import BigGAN512 

import torch 
import torchvision 

from scipy.stats import truncnorm 

import argparse 

def gen(class_label):
    pretrained_weight="biggan512-release.pt"
    size=512
    truncation=0.4
    output='output/'+str(class_label)
    truncation = torch.clamp(torch.tensor(truncation), min=0.02+1e-4, max=1.0-1e-4).float()  
    c = torch.tensor((class_label,)).long()

    if size == 128: 
        z = truncation * torch.as_tensor(truncnorm.rvs(-2.0, 2.0, size=(1, 120))).float() 
        biggan = BigGAN128() 
    elif size == 256: 
        z = truncation * torch.as_tensor(truncnorm.rvs(-2.0, 2.0, size=(1, 140))).float() 
        biggan = BigGAN256()
    elif size == 512: 
        z = truncation * torch.as_tensor(truncnorm.rvs(-2.0, 2.0, size=(1, 128))).float() 
        biggan = BigGAN512() 

    biggan.load_state_dict(torch.load(pretrained_weight)) 
    biggan.eval() 
    with torch.no_grad(): 
        img = biggan(z, c, truncation.item())  

    img = 0.5 * (img.data + 1) 
    pil = torchvision.transforms.ToPILImage()(img.squeeze())
    if output is not None:
        pil.save(output + ".jpg")
    

