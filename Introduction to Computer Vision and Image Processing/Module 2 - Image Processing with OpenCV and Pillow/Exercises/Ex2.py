
#Question 1:
#Use the image baboon.png from this lab or take any image you like.

#Open the image and create a PIL Image object called im, flip im and create an image called im_flip. Mirror im and create an image called im_mirror. Finally, plot both images.

# write your script here
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

im = Image.open("lenna.jpg")

im_flip = ImageOps.flip(im)
plt.figure(figsize=(5,5))
plt.imshow(im_flip)
plt.show()

im_mirror = ImageOps.mirror(im)
plt.figure(figsize=(5,5))
plt.imshow(im_mirror)
plt.show()