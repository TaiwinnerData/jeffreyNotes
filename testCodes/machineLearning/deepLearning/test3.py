# This is the simplest neural network.
import numpy as np
from sklearn import datasets
import pandas as pd


# define basic math function including differential methods.
# the below function only works for two dimensional problems.
def f_px_diff(f_funct, f_x, f_y):
    dx = 0.001
    df = f_funct(f_x + dx, f_y) - f_funct(f_x, f_y)
    return df/dx

def f_py_diff(f_funct, f_x, f_y):
    dy = 0.001
    df = f_funct(f_x, f_y + dy) - f_funct(f_x, f_y)
    return df/dy

def f_px_diff_loss(f_funct, f_x, f_y, f_dataset):
    dx = 0.001
    df = f_funct(f_dataset, f_x + dx, f_y) - f_funct(f_dataset, f_x, f_y)
    return df/dx

def f_py_diff_loss(f_funct, f_x, f_y, f_dataset):
    dy = 0.001
    df = f_funct(f_dataset, f_x, f_y + dy) - f_funct(f_dataset, f_x, f_y)
    return df/dy

def GD(f_funct, n, r):
    xn, yn = 10, 10
    vn = np.array([xn, yn])
    for i in range(n):
        vn = vn - r*np.array([f_px_diff(f_funct, vn[0], vn[1]), f_py_diff(f_funct, vn[1], vn[0])])
    return vn

def GD_loss(f_funct, n, r, f_dataset):
    xn, yn = 10, 10
    vn = np.array([xn, yn])
    for i in range(n):
        gradient = np.array([f_px_diff_loss(f_funct, vn[0], vn[1], f_dataset), f_py_diff_loss(f_funct, vn[0], vn[1], f_dataset)])
        gradient = gradient/(gradient[0]**2 + gradient[1]**2)**(1/2)
        vn = vn - r*gradient
    return vn

# for m = w1/w2 and b is the bias
def loss_funct(f_data, m, b):
    total_result = 0
    for i in range(len(f_data)):
        total_result = total_result + (f_data[i][1] - (b-m*f_data[i][0]))**2
    return total_result


# ----------------------------------------------------------------------------------
# load data set
test_data = pd.read_csv("weight-height.csv")
test_data = pd.DataFrame.to_numpy(test_data)

test_data = test_data[:100, 1:3]




# ----------------------------------------------------------------------------------
# execute the result
def main():
    print(test_data)
    GD_result = GD_loss(loss_funct, 100, 0.01, test_data)
    print(GD_result)
    print("for  weight = 70, guess the height:")
    print(GD_result[1] - GD_result[0]*70)








if __name__ == "__main__":
    main()
    





