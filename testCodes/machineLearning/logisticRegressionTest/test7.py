# Load libraries
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np


# Load(or create) dataset
x = [1, 2, 4, 6, 10]

x = [
        [1, 2],
        [2, 4],
        [4, 8],
        [6, 12],
        [3, 3],



        [4, 4],
        [5, 5],
        [8, 8],
        [10, 10]
        ]
y = [
        [1],
        [1],
        [1],
        [1],
        [0],


        [0],
        [0],
        [0],
        [0]
        ]
x = np.array(x)
y = np.array(y)
print(x)
print(y)

# Create test dataset
test_x = [11, 12, 13, 14, 16]

test_x = [
        [11, 23],  # 1
        [12, 24],  # 1
        [13, 1],   # 0
        [14, 28],  # 1
        [2, 4]     # 1
        ]


test_x = [
        [11, 23],  # 1
        [12, 24],  # 1
        [13, 1],   # 0
        [14, 28],  # 1
        [2, 4],    # 1
        [3, 7],    # 1
        [16, 30],  # 1
        [11, 24],  # 1
        [13, 13]   # 0
        ]

test_x = np.array(test_x)


# Create logistic model
logistic_model = LogisticRegression(random_state=0)

# Use training model
logistic_model.fit(x, y)

# Use training data to predict classification.
predicted = logistic_model.predict(test_x)
print("show predicted value of input x list")
print(predicted)
print("-"*30)

# Show the coeffecient of the model
print("Show coefficients")
result_coef = logistic_model.coef_
result_intercept = logistic_model.intercept_
print(logistic_model.coef_, logistic_model.intercept_)
print("show coef_.T")
print(logistic_model.coef_.T)
print("show coef_")
print(logistic_model.coef_)

# Show the result.
#print("training set: ", logistic_model.score(x_train, y_train))
#print("training set: ", logistic_model.score(x_validation, y_validation))


w1 = logistic_model.coef_[0][0]
w2 = logistic_model.coef_[0][1]
b = result_intercept
# calculate the coefficients of the fit line
c = -b/w2
m = -w1/w2
# the fit equations should be like this:
# w1*x + w2*y + b = 0, 
# and so we want to draw the fit line as  y = -w1/w2 * x - b/w2



# Show diagram
plt.scatter(test_x[:, 0], test_x[:, 1], s=1)
plt.plot(test_x[:, 0], test_x[:,0]*m+c, linewidth='0.5')
plt.show()

