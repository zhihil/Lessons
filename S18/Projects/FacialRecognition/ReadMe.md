# Goal
The goal of this project is to create an algorithm that can be used to recognized individual's faces, but more importantly to be able to explain how such an algorithm is working.
The actual algorithm itself can be coded in less than 50 lines of code: primarily by offloading some of the training and complexity to a clould machine learning service such as Clarifai.
To be able to understand the algorithm we will be working through various concepts in deep learning that are necessary to read Google's FaceNet paper (the inspiration and backbone of this project.)

We'll want to understand:
  - What is an artificial neuron
  - What is the difference between a perceptron and a multi-layer perceptron (MLP)
  - How to train an MLP using the backpropagation algorithm
  - How to leverage existing libraries to build and train neural networks (keras)
  - What is a convolutional neural network and why they are useful in computer vision
  - What are standard practices for training a neural network (weight initzilization, regularization, data normalization, mini batches, data augmentation, etc)
  - What are the different kind of loss functions and when to use them
  - How to use Keras built-in functions to perform standard practices
  - (Time permitting) How to find a suitable dataset and clean it up for further analysis
  - How get an API key from Clarifai, and access their service
  - (Time/Money Permitting) How to train a network using data provided by Clarifai
  - How to make a simple UI to showcase the project

## Required Software
We will be using Python with the following libraries:
  - Numpy
  - Matplotlib
  - H5Py
  - Keras
  - Tensorflow
  - Clarifai
  - Jupyter
  - openCV

# Session 1

We will be using Python as the main language for this project. 
We will need to install a couple of libraries on top of that to get started; for this week:
  - Numpy
  - Matplotlib
  - Jupyter

# Session 2
We will cover the backpropagation algorithm, and run through an example on paper before building a simple MLP to solve the XOR problem.
Then we will use Keras to do the same in a fraction of the time.

# Session 3
We will take a look at the MNIST (hand-written digit classification) dataset. We will cover the advantages of convolutional neural networks (CNN)  and describe the basic architecture.
We'll use Keras again to compare MLPs vs CNNs.
Time-permitting we'll start talking about regularization, and data augmentation.

# Session 4
We'll poke around in Keras using the MNIST dataset to try and tease out differences from weight-initialization, data normalization, mini batches, etc.
Cover regularization and data augmentation.

# Session 5
Talk about some state of the art architectures (AlexNet, ResNet, Inception)
Find a suitable dataset and clean it up (Time permitting)

# Session 6
How to get a clarifai key and use it.
Building a simple UI

# Session 7
Slack time
