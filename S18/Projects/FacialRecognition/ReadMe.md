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

## Week by Week
| Lesson # | Week # | Date          | Description                                    |
| :------- | ------ | ------------- | ---------------------------------------------- |
| -        | 4      | May 23, 2018  | Introductions & Sign-ups                       |
| 1        | 5      | May 30, 2018  | Python installation, introduciton to perceptron |
| 2        | 6      | June 6, 2018  | Backprop, gradient descent, MLP from scratch, intro to Keras|
| -        | 7      | June 13, 2018 | '-- Hell Week --' |
| 3        | 8      | June 20, 2018 | MNIST, MLPs vs CNNs, regularization |
| 4        | 9      | June 27, 2018 | Data normalization, weight-initizilization, batches, data augmentation |
| 5        | 10     | July 4, 2018  | Data munging on Faces in the Wild |
| 6        | 11     | July 11, 2018 | Clarifai, building a simple UI |
| 7        | 12     | July 18, 2018 | Catch-up and polishing time                    |
| -        | 13     | July 25, 2018 | End of Term Event!                             |

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
Cleaning up Faces in the Wild. Programming exercise to do data normalization and preparation before building our neural network.

# Session 6
How to get a clarifai key and use it.
Building a simple UI

# Session 7
Slack time
