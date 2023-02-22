import numpy as np
import pandas as pd
import random as random
from sklearn import datasets


def digit_classification(input_y):
    output = np.empty((len(input_y), 10))
    for i in range(len(input_y)):
        for j in range(10):
            if input_y[i] == j:
                output[i][j] = 1
            else:
                output[i][j] = 0
    return output


class NN():
    def __init__(self):
        # declare 
        self.feature_size = 64
        self.hidden_size = 50
        self.output_size = 10

        # declare weights
        self.w1_2 = np.random.randn(self.feature_size, self.hidden_size)
        self.w2_3 = np.random.randn(self.hidden_size, self.output_size)

    def _sigmoid(self, z):
        return 1/(1+np.exp(-z))

    def _diff_sigmoid(self, z):
        return self._sigmoid(z)*(1-self._sigmoid(z))

    def _forward_propagation(self, input_X):
        # layer 1
        self.net1 = input_X
        # layer 2
        self.net2 = np.dot(self.net1, self.w1_2)
        self.o2 = self._sigmoid(self.net2)
        # layer 3
        self.net3 = np.dot(self.o2, self.w2_3)
        self.o3 = self._sigmoid(self.net3)

    def _backward_propagation(self, input_y):
        # layer 3
        predict = self.o3
        delta = predict - input_y
        self.delta3 = np.multiply(delta, self._diff_sigmoid(self.net3))
        # layer 2
        self.delta2 = np.multiply(np.dot(self.delta3, self.w2_3.T), self._diff_sigmoid(self.net2))

        # create gradient of the weights
        m = self.net1.shape[0]
        self.w1_2_grad = np.dot(self.net1.T, self.delta2)/m
        self.w2_3_grad = np.dot(self.net2.T, self.delta3)/m

    def _update(self, learning_rate=0.0001):
        self.w1_2 = self.w1_2 - learning_rate*self.w1_2_grad
        self.w2_3 = self.w2_3 - learning_rate*self.w2_3_grad

    def train(self, input_X, input_y, iteration):
        for i in range(iteration):
            self._forward_propagation(input_X)
            self._backward_propagation(input_y)
            self._update()
        
    def predict(self, input_X):
        self._forward_propagation(input_X)
        y_pred = self.o3
        print("show y_pred")
        print(y_pred)
        y_output_pred = []
        for i in range(len(input_X)):
            y_output_pred.append(y_pred[i].argmax(axis=0))
        return y_output_pred

def main():
    # import digits datasets
    train_size = 300
    test_size = 5 

    digits = datasets.load_digits()
    digits_X = digits.data
    digits_y = digits.target
    result_y = digits_y[train_size:train_size+test_size]


    # create neural network model
    testNN = NN()
    digits_y = digit_classification(digits_y)

    # spliting train data and test data
    train_X = digits_X[:train_size]
    train_y = digits_y[:train_size]

    test_X = digits_X[train_size:train_size+test_size]
    test_y = digits_y[train_size:train_size+test_size]


#    result_y = digits_y[train_size:train_size+test_size]
    testNN.train(train_X, train_y, 50)
    predict_result = testNN.predict(test_X)
    print(predict_result)
    print(result_y)
#    print(testNN.o3)


if __name__ == "__main__":
    main()



