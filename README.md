# BigGAN-Pretrained
Uses a Pretrained Network (Trained using Google's Deepmind) to generate images. 

# BigGAN

The BigGAN is an implementation of the GAN architecture designed to leverage the best from what has been reported to work more generally.
Specifically, the BigGAN is designed for class-conditional image generation. That is, the generation of images using both a point from latent space and image class information as input. Example datasets used to train class-conditional GANs include the CIFAR or ImageNet image classification datasets that have tens, hundreds, or thousands of image classes.

As its name suggests, the BigGAN is focused on scaling up the GAN models.

This includes GAN models with:

- More model parameters (e.g. more feature maps).
- Larger Batch Sizes
- Architectural changes

For more info refer to [paper](https://arxiv.org/abs/1809.11096)

# Download Pretrained Weights 
The Pretrained weights can be downloaded from [here](https://github.com/ivclab/BigGAN-Generator-Pretrained-Pytorch/releases/latest)

# Installation
This requires anaconda or miniconda.

To create the environement run
```
conda env create -f environement.yml
```

The following dependencies will be installed:
  - python=3.6
  - cudatoolkit=10.0
  - pytorch
  - torchvision
  - scipy
  
# Usage
To run the code, download the pretrained weights first.

```
python generate.py -w <PRETRAINED_WEIGHT_PATH> [-s IMAGE_SIZE] [-c CLASS_LABEL] [-t TRUNCATION] [-o OUTPUT_FILE] 
```

For example:
```
python generate.py -w ./biggan512-release.pt -s 512 -t 0.3 -c 156 
python generate.py -w ./biggan256-release.pt -s 256 -t 0.02 -c 11 -o output
``` 
The Valid parameters are:
- Valid image size: 128, 256, 512
- Valid class label: 0~999
- Valid truncation: 0.02~1.0

## Examples
<p align="center">
<img src="https://github.com/crypto-code/BigGAN-Pretrained/blob/master/assets/156.jpg" width="400" height="400" align="middle"/>  </p>
<p align="center"><b>Class 156</b></p>

<p align="center">
<img src="https://github.com/crypto-code/BigGAN-Pretrained/blob/master/assets/292.jpg" width="400" height="400" align="middle"/>  </p>
<p align="center"><b>Class 292</b></p>

<p align="center">
<img src="https://github.com/crypto-code/BigGAN-Pretrained/blob/master/assets/972.jpg" width="400" height="400" align="middle"/>  </p>
<p align="center"><b>Class 972</b></p>
                 
<p align="center">
<img src="https://github.com/crypto-code/BigGAN-Pretrained/blob/master/assets/992.jpg" width="400" height="400" align="middle"/>  </p>
<p align="center"><b>Class 992</b></p>


# G00D LUCK

For doubts email me at:
atinsaki@gmail.com
