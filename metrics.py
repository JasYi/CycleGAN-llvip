from math import log10, sqrt
import cv2
import numpy as np
import sys
from skimage.metrics import structural_similarity as ssim
import os
from SSIM_PIL import compare_ssim
from PIL import Image

def PSNR(original, compressed): 
    mse = np.mean((original - compressed) ** 2) 
    if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                  # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse)) 
    return psnr 

result_path = sys.argv[1]

flag = False
first_img = None
second_img = None
first_ssim = None
second_ssim = None
PSNR_agg = 0
SSIM_agg = 0
counter = 0

for images in sorted(os.listdir(result_path)):
    if flag:
        second_img = cv2.imread(result_path + "/" + images)
        second_img = cv2.resize(second_img, (256, 256))
        second_ssim = Image.open(result_path + "/" + images)
        second_ssim = second_ssim.resize((256, 256))
        PSNR_agg += PSNR(first_img, second_img)
        SSIM_agg += compare_ssim(first_ssim, second_ssim)
        counter += 1
        flag = False
    else:
        first_img = cv2.imread(result_path + "/" + images)
        first_ssim = Image.open(result_path + "/" + images)
        flag = True

print(f"Average PSNR: {PSNR_agg / counter}")
print(f"Average SSIM: {SSIM_agg / counter}")