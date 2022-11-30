# This test is for figuring out the difference between the method of the VSM and logistic regression.
# It seems like VSM and Logistic regression all are trying to find out the fitted line of the different
# classification data. But it seems like they are using differnet method to find the fitted line. And it
# also seems like they are using different method to decide the classification value in the end.


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_blobs


# Create datasets from sklearn blobs function.
samples_number = 1000
x, y = make_blobs(n_samples=samples_number, centers=2, n_features=2, random_state=100, cluster_std=0.5, center_box=(-1, 1))
split_point = int(samples_number/2)
# x training data.
train_x = x[0:split_point]
train_y = y[0:split_point]
train_y = train_y.reshape(-1, 1)
# x testing data
test_x = x[split_point:]
test_y = y[split_point:]
test_y = test_y.reshape(-1, 1)
# Create svm model
svm_model = SVC(kernel='linear', C=1.0)
# Create Logistic model
logistic_model = LogisticRegression(random_state=0)


# Now I want to compare to model and find the difference between them.
svm_model.fit(train_x, train_y)
logistic_model.fit(train_x, train_y)
print("Show the prediction result of two model, vsm model and logistic model.")
print("-"*100)
print("-"*100)
# Suppose the line of the separation data of the model is like w1*x1 + w2*x2 + b = 0
# and so the separation line can be written as x2 = -w1/w2*x1 - b/w2  =  m*x1 + c

# svm model
print("svm model:")
print("coef_:")
print(svm_model.coef_)
print("intercept_:")
print(svm_model.intercept_)
print("predict:")
print(svm_model.predict(test_x))
print("-"*100)
# logistic model
print("logistic model:")
print("coef_:")
print(logistic_model.coef_)
print("intercept_:")
print(logistic_model.intercept_)
print("predict:")
print(logistic_model.predict(test_x))
