import numpy as np
import cv2
from argparse import ArgumentParser

# defining the function, input two gray images and c1,c2, output the structure similarity of two images
def SSIM(A, B, c1, c2):
    mean_A = np.mean(A)
    mean_B = np.mean(B)
    covAB = np.cov(A.flatten(), B.flatten(), ddof=0)[0][1]
    var_A = float(np.cov(A.flatten(), ddof=0))
    var_B = float(np.cov(B.flatten(), ddof=0))
    L = 255
    ans = (2*mean_A*mean_B+(c1*L)**2)*(2*covAB+(c2*L)**2)/((mean_A)**2+(mean_B)**2+(c1*L)**2)/(var_A+var_B+(c2*L)**2)
    return ans

parser = ArgumentParser(usage="SSIM.py [-h] [img1 filename] [img2 filename]", description="messure the structure similarity of two gray images")

parser.add_argument("pos1", help="img1 filename")
parser.add_argument("pos2", help="img2 filename")

args = parser.parse_args()

img1 = cv2.imread(args.pos1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(args.pos2, cv2.IMREAD_GRAYSCALE) 
img2 = cv2.resize(img2, img1.shape)

cv2.namedWindow('img1', cv2.WINDOW_NORMAL)
cv2.imshow('img1', img1)
cv2.namedWindow('img2', cv2.WINDOW_NORMAL)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Its structure similarity is {}".format(SSIM(img1, img2, 1, 1)))
