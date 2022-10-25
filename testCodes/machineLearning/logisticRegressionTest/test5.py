# Load libraries
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np


# Load(or create) dataset
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
x = np.array(x)
y = np.array(y)
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

# Create test dataset
test_x = [11, 12, 13, 14]
test_x = np.array(test_x)
test_x = test_x.reshape(-1, 1)
print(test_x)


# Create logistic model
logistic_model = LogisticRegression(random_state=0)

# Use training model
logistic_model.fit(x, y)

# Use training data to predict classification.
predicted = logistic_model.predict(test_x)
print("show predicted value of input x list")
print(predicted)

# Show the result.
#print("training set: ", logistic_model.score(x_train, y_train))
#print("training set: ", logistic_model.score(x_validation, y_validation))
