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

    def _sigmoid(self, z):
        return 1/(1+np.exp(-z))

    def _diff_sigmoid(self, z):
        return self._sigmoid(z)*(1-self._sigmoid(z))

    def _forward_propagation(self, X_input): # 
        # layer 1
        self.net1 = (X_input-120)*0.01  # why should i do this?  # this is actually normalization. without this it's hard to train.
#        self.net1 = X_input*0.01
        self.net2 = np.dot(self.net1, self.w1_2)
        self.net2 = np.float64(self.net2) # change the data type to numpy's float or the _simgoid can't read it.
        self.o2 = self._sigmoid(self.net2)
        
        # layer 2
        self.net3 = np.dot(self.o2, self.w2_3)
        self.net3 = np.float64(self.net3)
        self.o3 = self._sigmoid(self.net3)

    def _backward_propagation(self, y):
        predict = self.o3
#        delta = y-predict
        delta = predict-y   # what is the difference between "predict-y" and "y-predict"??? 
        self.delta3 = np.multiply(delta, self._diff_sigmoid(self.net3))
        self.delta2 = np.multiply(np.dot(self.delta3, self.w2_3.T), self._diff_sigmoid(self.net2))

        # create gradient
        m = self.net1.shape[0]   # m is for the normalization of gradient
        self.w1_2_grad = np.dot(self.net1.T, self.delta2)*(1/m)
        self.w2_3_grad = np.dot(self.net2.T, self.delta3)*(1/m)

#        self.w1_2_grad = np.dot(self.net1.T, self.delta2)
#        self.w2_3_grad = np.dot(self.net2.T, self.delta3)

    def _update(self, learning_rate=10):
        self.w1_2 = self.w1_2 - learning_rate*self.w1_2_grad
        self.w2_3 = self.w2_3 - learning_rate*self.w2_3_grad

    def train(self, X, y, iteration):
        for i in range(iteration):
            self._forward_propagation(X)
            print("show o3 before backward")
            print(self.o3)
            self._backward_propagation(y)
            self._update()
            print("-"*100)

    def predict(self, X):
        self._forward_propagation(X)
        y_pred = self.o3
        for i in range(len(X)):
            if y_pred[i] >= 0.5:
                y_pred[i] = 1
            else:
                y_pred[i] = 0
        return np.array(y_pred)

    def accuracy(self, predict, y):
        cnt = np.sum(predict==y)
        return (cnt/len(y))*100


def main():
    # import datasets
    datasets = pd.read_csv("weight-height.csv")
    datasets = pd.DataFrame.to_numpy(datasets)
#    np.random.seed(30)
    np.random.shuffle(datasets)

    train_number = 30  # 100 original
    train_X, train_y = datasets[:train_number, 1:3], datasets[:train_number, 0:1]


    test_number = 100
    test_X, test_y = datasets[train_number:train_number+test_number, 1:3], datasets[train_number:train_number+test_number, 0:1]


    # turn all the y value to 0 or 1
    for i in range(train_number):
        if train_y[i] == "Male":
            train_y[i] = 1
        else:
            train_y[i] = 0

    testNN = NN()
    iteration = 30
    testNN.train(train_X, train_y, iteration)

    # turn all the y value to 0 or 1
    print(test_y)
    for i in range(test_number):
        if test_y[i] == "Male":
            test_y[i] = 1
        else:
            test_y[i] = 0

    predict_y = testNN.predict(test_X)
    print(predict_y)
    accuracy = testNN.accuracy(predict_y, test_y)
    print("accuracy: " + str(accuracy) + " %")
    print("weights")
    print(testNN.w1_2)
    print(testNN.w2_3)
    print("gradient")
    print(testNN.w1_2_grad)
    print(testNN.w2_3_grad)

if __name__ == "__main__":
    main()
