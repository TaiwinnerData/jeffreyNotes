# when I use linear regression i can get the prediction result by inputing x and find y
# in logistic regression we can't do just inputing x and get y, we can only get 1 or 0(well something like that)

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# create basic datasets
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
x = np.array(x)
y = np.array(y)
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
print("x")
print(x)
print("y")
print(y)

# create test datasets
test_x = [11, 12, 13, 14, 15]
test_x = np.array(test_x)
test_x = test_x.reshape(-1, 1)
print("test_x")
print(test_x)



# create linear regression model
model = linear_model.LinearRegression()
model.fit(x, y)
predicted_result = model.predict(test_x)
print("predicted result")
print(predicted_result)


