# Module 4 - Neural Networks and Deep Learning for Image Classification

# Neural Networks

A neural network is a type of machine learning model that’s inspired by the structure of the human brain. It's made up of layers of interconnected nodes (also called neurons) that process data and learn patterns from it.

# **Simple Neural Network for XOR**

Completed Lab; attached to Module

# Fully Connected Neural Network Architecture

- Deals with how to arrange the different number of hidden layers and neurons
- We can make multiclass predictions using neural networks, just by adding more neurons to the output layer
- A neural network with mroe than one hidden layer is known as a deep neural network
    - More neurons or more layers may lead to overfitting
    - The output or activation of each layer is the same dimension as the number of neurons

# **Neural Network Rectified Linear Unit (ReLU) vs Sigmoid**

Completed Lab; attached to module

# Training a Neural Network with Momentum

Completed Lab; attached to module

# Convolutional Neural Networks (CNNs)

A CNN is a neural network with special layers - A CNN looks at small parts of an image, finds important features, reduces complexity, and then uses those features to figure out what the image is.

- Convolution and pooling layers are the first layers used to extract features from an input these can be thought of as the feature learning layers, the fully connected layers are simply a neural network

# Convolutional Neural Network Lab

Completed Lab; attached to module

# Data Augmentation

Completed Lab; attached to module

# CNN Architectures

Popular Architectures include:

- LeNet-5
    - One of the first CNNs.
    - Used on MNIST (handwritten digits dataset).
- AlexNet
    - Deep network with large kernels (e.g., 11×11) and many parameters
    - Needs lots of data to train
    - Sparked the revival of CNNs in image classification
- VGGNet
    - Known for being deeper and simpler.
    - VGG-16 and VGG-19 are most common
    - Uses stacked 3×3 convolutions instead of larger ones
        - Same effect (receptive field) but fewer parameters and faster training
- Resnet
    - As networks got deeper, vanishing gradients became an issue
    - ResNet solves this using skip connections
    - Allows for very deep networks (e.g., 32+ layers) to be trained effectively

# Practice Assessment

![image.png](image.png)

![image.png](image%201.png)

# ChatGPT Q&A

[https://chatgpt.com/share/68198483-fb3c-8001-91a6-00d046cf99fd](https://chatgpt.com/share/68198483-fb3c-8001-91a6-00d046cf99fd)