# Embeddings

**Embeddings are** lower-dimensional representations of sparse data

# Embedding Space and Static Embeddings

An [**embedding**](https://developers.google.com/machine-learning/glossary#embedding-vector) is a vector representation of data in [**embedding space**](https://developers.google.com/machine-learning/glossary#embedding-space). Generally speaking, a model finds potential embeddings by projecting the high-dimensional space of initial data vectors into a lower-dimensional space

Embeddings make it easier to do machine learning on large [**feature vectors**](https://developers.google.com/machine-learning/glossary#feature-vector)

You do not need to apply an activations function on the embedding layer

# Obtaining Embeddings

### Training an embedding as part of a neural network

You can create an embedding while training a [**neural network**](https://developers.google.com/machine-learning/crash-course/neural-networks) for your target task. This approach gets you an embedding well customized for your particular system, but may take longer than training the embedding separately.

In general, you can create a hidden layer of size *d* in your neural network that is designated as the [**embedding layer**](https://developers.google.com/machine-learning/glossary#embedding-layer), where *d* represents both the number of nodes in the hidden layer and the number of dimensions in the embedding space. This embedding layer can be combined with any other features and hidden layers. As in any deep neural network, the parameters will be optimized during training to minimize loss on the nodes in the network's output layer.

# ChatGPTQ&A

[https://chatgpt.com/share/680a373f-994c-8001-879d-e465b02103e8](https://chatgpt.com/share/680a373f-994c-8001-879d-e465b02103e8)

# Completion

![image.png](image.png)