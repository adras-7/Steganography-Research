# Module 5 - Object Detection

# Object Detection

- Sliding Windows
    - Slides a fixed-size window across the image
    - Each window is classified:
        - If object (e.g., dog) is present → label as "dog"
        - If no object → label as "background"
    - Moves across the image row by row, left to right, top to bottom
- Bounding Box
    - A rectangle around the detected object
    - Goal of detection: Predict bounding box coordinates for each object
- Bounding Box Pipeline
    - Start with a dataset of images, object labels, and bounding boxes
    - Train a model to learn both the object class and box coordinates
    - At prediction time, the model outputs:
        - Predicted class (e.g., dog, cat)
        - Predicted bounding box (location of object)
- Score
    - Each detection comes with a confidence score (0 to 1) → higher condifence scores indicate higher confidence
    - You can set a threshold (e.g., 0.9) to filter out low-confidence predictions

# Objet Detection with Haar Cascade Classifier

A machine learning method where a cascade function is trained on a large number of positive images

- Trained on both positive and negative images
- Based on the Haar wavelet sequence: Haar wavelets are convolution kernels used to extract features. Haar wavelets extract information about: Edges, Lines, Diagonal edges

# Practice Assessment

![image.png](image.png)

![image.png](image%201.png)