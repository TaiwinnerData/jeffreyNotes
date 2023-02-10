import numpy as np
import pandas as pd
import sys
np.set_printoptions(threshold=np.inf)


# import height and weight datasets.
datasets = pd.read_csv("weight-height.csv")
datasets = pd.DataFrame.to_numpy(datasets)
datasets = datasets[5000:, 1:3] 
print(datasets)
total_weight = 0
total_height = 0
for i in range(len(datasets)):
    total_weight = total_weight + datasets[i][0]
    total_height = total_height + datasets[i][1]
average_weight = total_weight/len(datasets)
average_height = total_height/len(datasets)
print("average weight:")
print(average_weight)
print("average height:")
print(average_height)


#print(datasets)


# partial derivative for x of loss function
def p_x_diff_loss(funct, f_x, f_y, datasets):
    dx = 0.001
    df = funct(datasets, f_x+dx, f_y) - funct(datasets, f_x, f_y)
    return df/dx

# partial derivative for y of loss function
def p_y_diff_loss(funct, f_x, f_y, datasets):
    dy = 0.001
    df = funct(datasets, f_x, f_y+dy) - funct(datasets, f_x, f_y)
    return df/dy

# def loss function
def loss(datasets, m, b):
    total = 0
    for i in range(len(datasets)):
        total = total + (datasets[i][1] - (b+m*datasets[i][0]))**2
    return total

# def Gradient Descent method for loss function.
def GD_loss(funct, n, r, datasets):
    vn = [3, 5]
    vn = np.array(vn)
    for i in range(n):
        gradient = [p_x_diff_loss(funct, vn[0], vn[1], datasets), p_y_diff_loss(funct, vn[0], vn[1], datasets)]
        gradient = gradient/((gradient[0]**2 + gradient[1]**2)**(1/2))
        vn = vn - r*gradient
    return vn

def main():
    gradient_result = GD_loss(loss, 1000, 0.001, datasets)
    print(gradient_result)

    # trying to input a weight value and get the height value, for example weight = 70
    test_weight = 70
    print(gradient_result[1] + gradient_result[0]*test_weight)

if __name__ == "__main__":
    main()



