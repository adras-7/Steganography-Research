
#Question 1:
#Use the image lenna.png from this lab or take any image you like.

#Open the image and create a PIL Image object called blue_lenna, convert the image into a numpy array we can manipulate called blue_array, get the blue channel out of it, and finally plot the image

# write your code here
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

blue_lenna = Image.open('lenna.jpg')
blue_array = np.array(blue_lenna)
blue_array[:,:,2] = 0
plt.figure(figsize=(10,10))
plt.imshow(blue_array)
plt.show()