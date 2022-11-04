import numpy as np
import pandas as pd
import cvxopt
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
#from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

x = [
        [1, 2],
        [2, 4],
        [3, 6],
        [4, 8],
        [5, 10],
        [1, 1],
        [10, 11],
        [15, 15]
        ]

y = [
        [1],
        [1],
        [1],
        [1],
        [1],
        [0],
        [0],
        [0]
        ]

x = np.array(x)
y = np.array(y)

x_test = [
        [11, 22],
        [12, 24],
        [13, 13]
        ]
x_test = np.array(x_test)

#svm = LinearSVC.SVC()

# You should be able to use kernel='linear'.
svm = SVC(kernel='linear', C=1.0)
#svm = LogisticRegression()
svm.fit(x, y)
print(svm)
print(svm.predict(x_test))
