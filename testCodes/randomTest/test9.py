import numpy as np
import pandas as pd
#import cvxopt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix


# Load datasets from sklearn
x, y = make_blobs(n_samples=250, centers=100, random_state=0, cluster_std=0.60, n_features=4)
print(type(x))

# split dataset
x = x[0:150]
y = y[0:150]


y = y.reshape(-1, 1)

print(x)
print(y)
print(len(y))
