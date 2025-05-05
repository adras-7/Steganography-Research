# Module 2 - Image Processing with OpenCV and Pillow

# What is a Digital Image?

- A digital Image can be interpreted as a rectangular array of numbers
- Images are comprised of a rectangular grid of blocks called pixels
    - We can represent these pixels with numbers called intensity values
- An image can take on an almost unlimited number of values, but digital images have intensity values between zero and 255
- Pillow is a popular library for working with images in Python
- OpenCV is a library used for Computer Vision

# Image Processing with OpenCV - Ex1

Completed Lab Exercise - attached 

# Manipulating Images

- Copying allows you to create a new image independent of the original
- Flipping images changes the image’s orientation - We can flip an image by changing the index value of a pixel or intensity

# Manipulating Images One Pixel at a Time

- Cropping is cutting out the part of the image and throwing out the rest
- OpenCV can perform pixel manipulations

# Basic Image Manipulation with Pillow - Ex2

Completed Lab Exercise - attached 

# Basic Image Manipulation with OpenCV - Ex3

Completed Lab Exercise - attached

# Pixel Transformations

- Histograms:  A histogram counts the number of occurrences of a pixel, and it's a useful tool for understanding and manipulating images
- Intensity Transformations: An Intensity Transformation changes an image one pixel at a time. Some image transformations depend on neighbouring pixels

# Histograms and Intensity Transformations

Completed Lab Exercise

# Geometric Operations

- Geometric Transformation: We change the coordinates of the image x and y. In PIL we can scale the image by specifying the integer number of pixel’s using the method .resize()
- Geometric Scaling: Scaling is where we reshape the image, we can shrink or expand the image in a horizontal and or vertical direction. .resize() can also be used to scale an image in OpenCV or PIL
- Geometric Translation: Translation is where we shift the image, we can shift an image horizontally or vertically. In OpenCV, .warpAffine() allows you to translate an image by x pixels in the horizontal direction and y pixels in the vertical direction
- Geometric Rotation: Rotates an image by an angle theta. In OpenCV, .getRotationMAtrix2D() allows you to rotate an image by the angle inputted

# Geometric Transformations with Pillow

Completed Lab Exercise

# Spatial Operations in Image Processing

- Linear Filtering: Linear filtering applies a linear convolution between an image and a kernel (also called a mask or filter). The output pixel is a weighted sum of its neighbours, determined by the kernel.
- Edge Detection: Edge detection identifies areas of rapid intensity change. These areas often correspond to object boundaries in an image
- Median Filters: A non-linear filtering technique where the output pixel is the median of the surrounding neighbourhood. It’s effective for removing salt-and-pepper noise while preserving edges

# Practice Assessment Completion

![image.png](image.png)

![image.png](image%201.png)

# ChatGPT Q&A

[https://chatgpt.com/share/6818ae99-5ed4-8001-ba28-3af775924913](https://chatgpt.com/share/6818ae99-5ed4-8001-ba28-3af775924913)