# This is the simplest neural network.
import numpy as np
from sklearn import datasets
import pandas as pd


# define basic math function including differential methods.
# the below function only works for two dimensional problems.
def f_p_diff(f_funct, f_x, f_y):
    dx = 0.001
    df = f_funct(f_x + dx, f_y) - f_funct(f_x, f_y)
    return df/dx

def f_p_diff_loss(f_funct, f_x, f_y, f_dataset):
    dx = 0.001
    df = f_funct(f_dataset, f_x + dx, f_y) - f_funct(f_dataset, f_x, f_y)

def GD(f_funct, n, r):
    xn, yn = 0, 0
    vn = np.array([xn, yn])
    for i in range(n):
        vn = vn - [f_p_diff(f_funct, vn[0], vn[1]), f_p_diff(f_funct, vn[1], vn[0])]
    return vn

# for m = w1/w2 and b is the bias
def loss_funct(f_data, m, b):
    total_result = 0
    for i in range(len(f_data)):
        total_result = total_result + (f_data[1][i] - (b-m*f_data[0][i]))**2
    return total_result



# ----------------------------------------------------------------------------------
# load data set
test_data = pd.read_csv("weight-height.csv")
test_data = pd.DataFrame.to_numpy(test_data)
print(type(test_data))
print(test_data.shape)

test_data = test_data[:, 1:3]
print(test_data.shape)
print(test_data)




# ----------------------------------------------------------------------------------
# execute the result
def main():
    loss = loss_funct(test_data, 





