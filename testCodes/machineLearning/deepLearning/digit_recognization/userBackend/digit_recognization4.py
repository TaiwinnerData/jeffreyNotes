# this example use "backward propogation"
import numpy as np
import pandas as pd
import random as random
from sklearn import datasets
import cv2



def digit_classification(input_y):
    output = np.empty((len(input_y), 10))
    for i in range(len(input_y)):
        for j in range(10):
            if input_y[i] == j:
                output[i][j] = 1
            else:
                output[i][j] = 0
    return output


def reverse_digit_classification(input_y):
    output = np.empty((len(input_y), 1))
    for i in range(len(input_y)):
        for j in range(10):
            if input_y[i][j] == 1:
                output[i] = j 
    return np.transpose(output)[0]


class NN():
    def __init__(self):
        # declare 
        self.feature_size = 64
        self.hidden_size = 170 # the orinal is 10, but 25 is good
        self.output_size = 10

        # declare weights
        self.w1_2 = np.random.randn(self.feature_size, self.hidden_size)
        self.w2_3 = np.random.randn(self.hidden_size, self.output_size)

    def load_trainMD(self):
        self.w1_2 = np.load('w1_2.npy')
        self.w2_3 = np.load('w2_3.npy')

    def save_trainMD(self):
        np.save('w1_2', self.w1_2)
        np.save('w2_3', self.w2_3)

    def _sigmoid(self, z):
        return 1/(1+np.exp(-z))

    def _diff_sigmoid(self, z):
        return self._sigmoid(z)*(1-self._sigmoid(z))

    def _forward_propagation(self, input_X):
        # layer 1
#        self.net1 = (input_X-8)*0.01  # you could *0.1 or what
        self.net1 = (input_X-8)*0.01 # you could *0.1 or what

        # layer 2
        self.net2 = np.dot(self.net1, self.w1_2)
        self.net2 = np.float64(self.net2)
        self.o2 = self._sigmoid(self.net2)
        # layer 3
        self.net3 = np.dot(self.o2, self.w2_3)
        self.net3 = np.float64(self.net3)
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

    def _update(self, learning_rate): # learning rate originally 10
        self.w1_2 = self.w1_2 - learning_rate*self.w1_2_grad
        self.w2_3 = self.w2_3 - learning_rate*self.w2_3_grad

    def train(self, input_X, input_y, iteration):
        learning_rate = 10
        for i in range(iteration):
#            learning_rate = 10*((iteration-i)/(iteration-i))

            if i>1*iteration/7:
                learning_rate = 8 
            elif i>2*iteration/7:
                learning_rate = 4 
            elif i>3*iteration/7:
                learning_rate = 2
            elif i>4*iteration/7:
                learning_rate = 1
            elif i>5*iteration/7:
               learning_rate = 0.5
            elif i>6*iteration/7:
                learning_rate = 0.1

            self._forward_propagation(input_X)
            self._backward_propagation(input_y)
            self._update(learning_rate)
        
    def predict(self, input_X):
        self._forward_propagation(input_X)
        y_pred = self.o3
        print("show y_pred")
        print(y_pred)
        y_output_pred = []
        for i in range(len(input_X)):
            y_output_pred.append(y_pred[i].argmax(axis=0))
        return y_output_pred

    def accuracy(self, predict, y):
        cnt = np.sum(predict==y)
        return (cnt/len(y))*100

def main():
    # import digits datasets
#    train_size = 100
#    test_size = 10
#    train_size = 300 
    train_size = 300

#    test_size = 100 
    test_size = 3
    test_size = 100
#    test_size = 600
#    test_size = 700

    digits = datasets.load_digits()

    digits_X = digits.data
    print("length of digit_X")
    print(len(digits_X))
    digits_y = digits.target
    result_y = digits_y[train_size:train_size+test_size]
    print("show result_y")
    print(result_y)




    # create neural network model
    testNN = NN()
    print("digits_y before classification")
    print(digits_y)
    digits_y = digit_classification(digits_y)

    # test for reverse digit classfication
    test_reverse = reverse_digit_classification(digits_y)
    print("test reverse result")
    print(test_reverse)

    # spliting train data and test data
    train_X = digits_X[:train_size]
    train_y = digits_y[:train_size]

    test_X = digits_X[train_size:train_size+test_size]
    test_y = digits_y[train_size:train_size+test_size]
    print("test_X before shuffling")
    print(test_X)
    print("test_y before shuffling")
    print(test_y)


    # shuffle the test data
    total_test = np.concatenate((test_X, test_y), axis=1)
    print("-"*100)
    print("total_test")
    print(len(total_test))
    np.random.shuffle(total_test)
    test_X, test_y = total_test[:, 0:64], total_test[:,64:74]
    test_X = test_X[0:int(test_size/2)]
    test_y = test_y[0:int(test_size/2)]
    print("test_X after shuffling")
    print(test_X)
    print("show the type of test_X")
    print(type(test_X))
    print("test_y after shuffling")
    print(test_y)


#    result_y = digits_y[train_size:train_size+test_size]
    y_n_train_model = input("Are you want to retrain the model? y/n")
    iteration_number = 3000 # 1500 original # 3000 is good
    if y_n_train_model == "y":
        testNN.train(train_X, train_y, iteration_number)
        testNN.save_trainMD()
    else:
        testNN.load_trainMD()



    test_request = input("test current handwriting(y) or the datasets(n)?")
    if test_request == "y":
        # the following steps can change the images to the type that machine learning model can handle with
#        img = cv2.imread("digit_test_original2.png")
        img = cv2.imread("9_5.png")
        img = cv2.bitwise_not(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        img = np.transpose(img)
        img = img[0:1][0]
        print(img)
        print("-"*100)
        img = np.rot90(img, k=-1)
        img = np.fliplr(img)
        print("image transpose")
        print(img)
        img = img.flatten()
        img = img/3
        print(img)
        test_X = np.array([img])
        print("show test_X")
        print(test_X)
        predict_result = testNN.predict(test_X)
        print(predict_result)

        # now use the trained model to predict the final value


    else:
        print("-"*30)
        print("show the type of test_X")
        print(type(test_X))
        print(test_X)

        predict_result = testNN.predict(test_X)
        print("predict_result")
        print(predict_result)

        result_y = reverse_digit_classification(test_y)
        print("result_y")
        print(result_y)
    #    print(testNN.o3)
        print("accuracy")
    #    print(testNN.accuracy(predict_result, result_y))
        print(testNN.accuracy(predict_result, result_y))


    # save the weights and bias result as json files


if __name__ == "__main__":
    main()



