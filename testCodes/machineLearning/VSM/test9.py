# here's an example talk about how to use scatter_matrix
import numpy as np
import pandas as pd
import cvxopt
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
#from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_blobs

from pandas.plotting import scatter_matrix



# Load datasets from sklearn
samples_number = 1000 
x, y = make_blobs(n_samples=samples_number, centers=2, random_state=100, cluster_std=0.5, center_box=(-1, 1), n_features=2) # you can you n_features of make_blobs to change the number of the variables
print(x)
print(y)
#tt_split = int(samples_number/2)
#print(x[:, 0])

df = pd.DataFrame({
    "column1": x[:, 0],
    "column2": x[:, 1],
    #"column3": x[:, 2],
    "class": y
    })
print(df)
scatter_matrix(df)
plt.show()

