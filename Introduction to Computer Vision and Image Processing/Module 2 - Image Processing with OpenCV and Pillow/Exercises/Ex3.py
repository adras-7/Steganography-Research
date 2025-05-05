
#Question 4:
#Use the image baboon.png from this lab or take any image you like.

#Open the image and create a OpenCV Image object called im, convert the image from BGR format to RGB format, flip im vertically around the x-axis and create an image called im_flip, mirror im by flipping it horizontally around the y-axis and create an image called im_mirror, finally plot both images
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import cv2

im = cv2.imread("lenna.jpg")

im_flip =  cv2.flip(im, 0)
plt.imshow(cv2.cvtColor(im_flip, cv2.COLOR_BGR2RGB))
plt.show()

im_mirror =  cv2.flip(im, 1)
plt.imshow(cv2.cvtColor(im_mirror, cv2.COLOR_BGR2RGB))
plt.show()