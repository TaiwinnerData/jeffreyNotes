import numpy as np
from sklearn.linear_model import LinearRegression 

a = np.array([[5,8],[12,24],[19,11],[10,15]])

## weights
w = np.array([0.2, 0.5])

## bias  
b = 0.1  

y = np.matmul(w, a.T) + b

lr = LinearRegression()
lr.fit(a, y)

print(lr.coef_)
# array([0.2, 0.5])

print(lr.intercept_)
# 0.099
