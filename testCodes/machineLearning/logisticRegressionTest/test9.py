# This test is actually the final 
# Load libraries
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
import math as math


# Define sigmoid function to logistic regression usage
def sigmoid(x):
    return 1/(1+np.exp(-x))


# Load(or create) dataset, these datas are created by jeffrey for test.

# You should now use this kinda of data in logistic regression because it need two dimensions data to let it work
train_x = [1, 2, 4, 6, 10]

# This kinda data should work
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

# the sklearn packages only takes numpy array datas so you should turn the data into numpy array format, like this below
train_x = np.array(train_x)
train_y = np.array(train_y)
print(train_x)
print(train_y)



# Create test dataset, this data is created for test by jeffrey.
# And once again you need two dimensions data, the one dimension data wouldn't work.
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
logistic_model.fit(train_x, train_y)

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
# Show the scatter dots
plt.scatter(test_x[:, 0], test_x[:, 1], s=1)
# Show the fitted lines
plt.plot(test_x[:, 0], test_x[:,0]*m+c, 'r-', linewidth='0.5', label="fitted line")
#plt.plot(test_x[:, 0], test_x[:,0]*m+c+10, linewidth='0.5', label="test line")
# You have to add this line below to make label appeared in the plot
plt.legend()
#plt.show()





# the Logistic regression method is actually use sigmoid function to decide whether the data calculated result is 1 or 0
# show the "z = w1x1 + w2x2 + b"
print("-"*100)
print("z = w1*x1 + w2*x2 + b")
print("z = " + str(w1) + "x1"+ str(w2) + "x2" + "+" + str(b))
test_z = test_x[:, 0]*w1 + test_x[:, 1]*w2 + b
print("show test_z")
print(test_z)



# Show the "y = sigmoid(z) = 1/(1+exp(-z))
print("show sigmoid result of test_z")     
sigmoid_z = sigmoid(test_z)
print(sigmoid_z)
#for i in range(len(test_z)):
#    sigmoid_z[i] = f'{sigmoid_z[i]:.20f}'  # this script doesn't work.
#sigmoid_z = f'{sigmoid_z:.20f}'
print("show sigmoid result without scientific notation.")
np.set_printoptions(suppress=True)   # this line is for turnning the data from scientific notation into float.
print(sigmoid_z)
# showing y from sigmoid result the pass z value is 0.5

temp_result = []
for i in range(len(sigmoid_z)):
    if sigmoid_z[i] > 0.5:
        temp_result.append(1)
    else:
        temp_result.append(0)


print("show the prediction value from sigmoid method.")
print(temp_result)
