# Common Machine Learning Algorithms
* Perceptron
* K-Nearest Neighbor (KNN)
* Naive Bayes
* Decision Tree
* Hierarchical Clustering
* K-Means Clustering

## Table of contents
* [Background](#background)
* [Model](#model)
* [Algorithm](#algorithm-of-perceptron)
* [Convergence](#convergence-of-the-perceptron)
* [Dual Form](#dual-form-of-the-perceptron)

# Background
## The Birth of the Perceptron
![image](https://user-images.githubusercontent.com/70875733/137575694-5f4593c4-dfe9-4efc-9f8f-e0692aeaddc9.png)
<br><br>
* The Perceptron's Algorithm:
  * Frank Rosenblatt, Cornell Aeronautical Laboratory, 1957.
* Mark 1 Perceptron:
  * The first machine capable of having an original data

# Model
## The Model of the Perceptron
![image](https://user-images.githubusercontent.com/70875733/137575874-b9520f59-96c0-49ce-8bf8-c977a92ab37d.png) <br><br>
![image](https://user-images.githubusercontent.com/70875733/137575886-e527217c-40c0-4d4c-9b87-55702ab3f025.png)

## The Definition of the loss function
* The distance from any point to the hyperplane:
* The misclassified points: 
* The distance from a misclassified point to the hyperplane:
* The total distance from misclassiffied points to the hyperplane: 
* The loss function:
* The optimization goal:

## Optimization Algorithm
* The most common optimization algorithm is **Stochastic Gradient Descent (SGD)**
* At first, we calculate the derivative of the optimization function:
* And then, we randomly select a misclassified point ($x_i, y_i$) to update $w$ and $b$: $w <- w + \mu y_i x_i$
* Then $\mu (0 < \mu <= 1)$ is the learning rate.
* Other optimization algorithms: Adagrad, RMSprop, Adam, ...

# Algorithm of the Perceptron


# The Convergence of the Perceptron
# The Dual Form of the Perceptron
