<br><br><br>

# Using CycleGAN on the LLVIP Dataset

# CycleGAN and pix2pix in PyTorch

This work is heavily based on the work done by:

Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks.<br>
[Jun-Yan Zhu](https://www.cs.cmu.edu/~junyanz/)\*, [Taesung Park](https://taesung.me/)\*, [Phillip Isola](https://people.eecs.berkeley.edu/~isola/), [Alexei A. Efros](https://people.eecs.berkeley.edu/~efros). In ICCV 2017. (\* equal contributions) [[Bibtex]](https://junyanz.github.io/CycleGAN/CycleGAN.txt)

Image-to-Image Translation with Conditional Adversarial Networks.<br>
[Phillip Isola](https://people.eecs.berkeley.edu/~isola), [Jun-Yan Zhu](https://www.cs.cmu.edu/~junyanz/), [Tinghui Zhou](https://people.eecs.berkeley.edu/~tinghuiz), [Alexei A. Efros](https://people.eecs.berkeley.edu/~efros). In CVPR 2017. [[Bibtex]](https://www.cs.cmu.edu/~junyanz/projects/pix2pix/pix2pix.bib)

The original github repository this is forked from is https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

## Colab Notebook

The colab notebook can be found here: https://colab.research.google.com/drive/1bh0GYlusrWpQO-nRBK1HKRrHysOh1inr?authuser=1#scrollTo=0sp7TCT2x9dB

## Dataset

We have two LLVIP Datasets. The first dataset is the full LLVIP dataset and the second is a reduced version. The original LLVIP dataset has 12,025 paired test eaxmples, and 3,463 paired test examples. The reduced LLVIP dataset has 2,000 training examples per style and 1,463 test examples per style.

## SSIM and PSNR Metrics

We also created a script to automatically calculate the SSIM and PSNR of the test set. The script is `metrics.py`
