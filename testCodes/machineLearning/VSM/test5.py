# Here's an example talks about this, you should definitely understand the coefficients and the meaning of that:
# https://stats.stackexchange.com/questions/39243/how-does-one-interpret-svm-feature-weights
import numpy as np
import pandas as pd
import cvxopt
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
#from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

train_x = [
        [1, 2],
        [2, 4],
        [3, 6],
        [4, 8],
        [5, 10],
        [1, 1],
        [10, 11],
        [15, 15]
        ]

train_y = [
        [1],
        [1],
        [1],
        [1],
        [1],
        [0],
        [0],
        [0]
        ]

train_x = np.array(train_x)
train_y = np.array(train_y)

test_x = [
        [11, 22],
        [12, 24],
        [13, 13]
        ]
test_x = np.array(test_x)
#svm = LinearSVC.SVC()


# You should be able to use kernel='linear'.
svm = SVC(kernel='linear', C=1.0)
#svm = LogisticRegression()
svm.fit(train_x, train_y)


print(svm)
print(svm.predict(test_x))













# Show the coefficients of the model
print("show coefficient w of the model")
print(svm.coef_)
print("show coefficient b of the model")
print(svm.intercept_)

w1 = svm.coef_[0][0]
w2 = svm.coef_[0][1]
b = svm.intercept_

c = -b/w2
m = -w1/w2



# Suppose the line of the separation data of the model is like w1*x1 + w2*x2 + b = 0
# and so the separation line can be written as x2 = -w1/w2*x1 - b/w2  =  m*x1 + c

separate_x1 = test_x[:, 0]
separate_x2 = test_x[:, 1]


# show the diagram
plt.scatter(test_x[:, 0], test_x[:, 1], s=1)
# show the separate line
plt.plot(test_x[:, 0], test_x[:, 0]*m+c, 'r-', linewidth='0.5', label="fitted line") 
plt.legend()
plt.show()
