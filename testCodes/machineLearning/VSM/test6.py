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



# Training data for x
train_x = [
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


# Training data for y
train_y = [
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


# test data for x
test_x = [
[11, 23], 
[12, 24],
[13, 1],
[14, 28],
[2, 4],
[3, 7],
[16, 30],
[11, 24],
[13, 13]
]


test_y = [
        [1],
        [1],
        [0],
        [1],
        [1],
        [1],
        [1],
        [1],
        [0]
        ]

# turn the data to numpy array
train_x = np.array(train_x)
train_y = np.array(train_y)
test_x = np.array(test_x)
#svm = LinearSVC.SVC()


# You should be able to use kernel='linear'.
svm = SVC(kernel='linear', C=1.0)
#svm = LogisticRegression()
svm.fit(train_x, train_y)


print(svm)
print(svm.predict(test_x))
print("-"*100)




#---------------------------------------------------------------------------------------
# The code above is using svm function, the svm function would directly give you the predicted results about the model
# And in below you are about using the coefficients and intercept svm gave to you, and when you use the coefficients and intercept to form a separation functions, and you put the test value inside the function, you would get the same result as the predicted value that svm function gives to you.






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
plt.plot(test_x[:, 0], test_x[:, 0]*m+c, 'r-', linewidth='0.5', label="separation line") 
plt.legend()
#plt.show()


# Show the accuracy score of the model.
print("Show the accuracy of the model for train data and it should be 100% accuracy.")
print(svm.score(train_x, train_y))
print("Show the accuracy of the model for test data and it should random accuracy.")
print(svm.score(test_x, test_y))

# show the predicted value by the fit line plane.
predicted_value2 = w1*separate_x1 + w2*separate_x2 + b
print(predicted_value2)
for i in range(len(predicted_value2)):
    if predicted_value2[i]>0:
        predicted_value2[i] = 1
    else:
        predicted_value2[i] = 0


print("-"*30)
print(predicted_value2)



