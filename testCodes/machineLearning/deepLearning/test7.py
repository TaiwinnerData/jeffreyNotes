import numpy as np
import pandas as pd
import random as random


# Create neural network object class by using backward propagation.
class NN(object):
    def __init__(self):
        self.feature_number = 2  # feature numbers
        self.output_number = 1 # class number
        self.hidden_number = 3 # only single layer with 6 units

        # initilization matrix of weights In this case we have 2 layers of weights
        np.random.seed(1)
        self.w1_2 = np.random.randn(self.feature_number, self.hidden_number) # first layer's weights  2*2 matrix
        self.w2_3 = np.random.randn(self.hidden_number, self.output_number) # second layer's weights  2*1 matrix

    def _forward_propagation(self, x_input): # 
        # layer 1
        self.net1 = x_input 
        self.net2 = np.dot(self.net1, self.w1_2)
        self.net2 = np.float64(self.net2) # change the data type to numpy's float or the _simgoid can't read it.
        self.o2 = self._sigmoid(self.net2)
        
        # layer 2
        self.net3 = np.dot(self.o2, self.w2_3)
        self.net3 = np.float64(self.net3)
        self.o3 = self._sigmoid(self.net3)

    def _sigmoid(self, z):
        return 1/(1+np.exp(-z))

    def _diff_sigmoid(self, z):
        return self._sigmoid(z)*(1-self._sigmoid(z))

    def _backward_propagation(self, y):
        predict = self.o3
        delta = y - predict
        self.delta3 = np.multiply(delta, self._diff_sigmoid(self.net3))
        self.delta2 = np.multiply(np.dot(self.delta3, self.w2_3.T), self._diff_sigmoid(self.net2))

        # create gradient
        self.w1_2_grad = np.dot(self.net1.T, self.delta2)
        self.w2_3_grad = np.dot(self.net2.T, self.delta3)

    def _update(self, learning_rate=0.01):
#        self.w1_2 = self.w1_2 - np.multiply(learning_rate, self.w1_2_grad)
#        self.w2_3 = self.w2_3 - np.multiply(learning_rate, self.w2_3_grad)
        self.w1_2 = self.w1_2 - learning_rate*self.w1_2_grad
        self.w2_3 = self.w2_3 - learning_rate*self.w2_3_grad

    def train(self, X, y, iteration):
        for i in range(iteration):
            self._forward_propagation(X)
            self._backward_propagation(y)
            self._update()


#    def predict(self, X):
#        y_pred = self.


# import example data, for this test I use weight-height datasets.
# input the datasets
datasets = pd.read_csv("weight-height.csv")
datasets = pd.DataFrame.to_numpy(datasets)
np.random.shuffle(datasets)

# define train data
train_number = 2
train_X, train_y = datasets[:train_number, 1:3], datasets[:train_number, 0:1]

# define the test data
test_number = 200
test_X, test_y = datasets[train_number:train_number+test_number, 1:3], datasets[train_number:train_number+test_number, 0:1]

# turn all the y value to 1 or 0
for i in range(train_number):
    if train_y[i] == "Male":
        train_y[i] = 1
    else:
        train_y[i] = 0


def main():
    testNN = NN()
#    testNN._forward_propagation(train_X)
#    testNN._backward_propagation(train_y)

    testNN.train(train_X, train_y, 30)

    testData = np.array([64, 145])
    testNN._forward_propagation(testData)
    print("weight: " + str(testData[0]) + "height: " + str(testData[1]))
    if testNN.o3 > 0.5:
        print(testNN.o3)
        print(1)
        print("male")
    else:
        print(testNN.o3)
        print(0)
        print("female")








if __name__ == "__main__":
    main()
