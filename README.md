<br><br><br>

# Using CycleGAN on the LLVIP Dataset

- Maggie Shen xs196
- Jason Yi jsy37

# CycleGAN and pix2pix in PyTorch

This work is heavily based on the work done by:

Isola, P., Zhu, J.-Y., Zhou, T., & Efros, A. A. (2017). Image-to-Image Translation with Conditional Adversarial Networks. Conference on Computer Vision and Pattern Recognition. https://doi.org/https://doi.org/10.48550/arXiv.1611.07004 

Jia, X., Zhu, C., Li, M., Tang, W., & Zhou, W. (2021). LLVIP: A visible-infrared paired dataset for low-light vision. 2021 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW). https://doi.org/10.1109/iccvw54120.2021.00389 

Zhu, J.-Y., Park, T., Isola, P., & Efros, A. A. (2017). Unpaired image-to-image translation using cycle-consistent adversarial networks. 2017 IEEE International Conference on Computer Vision (ICCV). https://doi.org/10.1109/iccv.2017.244 

The original github repository this is forked from is https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

## Colab Notebook

Instructions on how to run the code can be found in the colab notebook.

The colab notebook can be found here: https://colab.research.google.com/drive/1bh0GYlusrWpQO-nRBK1HKRrHysOh1inr?authuser=1#scrollTo=0sp7TCT2x9dB

## Dataset

We have two LLVIP Datasets. The first dataset is the full LLVIP dataset and the second is a reduced version. The original LLVIP dataset has 12,025 paired test eaxmples, and 3,463 paired test examples. The reduced LLVIP dataset has 2,000 training examples per style and 1,463 test examples per style.

## SSIM and PSNR Metrics

We also created a script to automatically calculate the SSIM and PSNR of the test set. The script is `metrics.py`

## Slides

The slides to the presentation can be found here: https://docs.google.com/presentation/d/1O9bgmv8MsB9U3hb2igXc80aYukIb3_g7DYCzxg3MzAM/edit#slide=id.p

## Results
SSIM: 0.5362336975684212
PSNR: 28.236523251364066