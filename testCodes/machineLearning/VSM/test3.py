import numpy as np
import pandas as pd
#import cvxopt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix


# Load dataset
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
#dataset = pd.read_csv(url, namees = names)

x, y = make_blobs(n_samples=250, centers=2, random_state=0, cluster_std=0.60)
print("show data of x")
print(x)
print("show data of y")
print(y)

# Split dataset
#array = dataset.values
#x = array[:, 0:4]
#y = array[:, 4]

y[y == 0] = -1

tmp = np.ones(len(x))

y = tmp * y

#print("show data of x")
#print(x)
#print("show data of y")
#print(y)
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='winter')
plt.show()

#print("show data of x")
#print(x)
#print("show data of y")
#print(y)
