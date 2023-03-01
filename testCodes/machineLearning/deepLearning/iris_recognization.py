import pandas as pd
import numpy as np
from sklearn import datasets as ds



# define classfication function
def iris_classification(input_y):
    output = np.empty((len(input_y), 3))
    for i in range(len(input_y)):
        for j in range(3):
            if input_y[i] == j:
                output[i][j] = 1
            else:
                output[i][j] = 0
    return output


# create neural network object by backward propagation.
class NN(object):
    def __init__(self):
        self.feature_size = 4
        self.hidden_size = 5
        self.output_size = 3

        # initialize the weights
        self.w1_2 = np.random.randn(self.feature_size, self.hidden_size)
        self.w2_3 = np.random.randn(self.hidden_size, self.output_size)

    def _sigmoid(self, z):
        return 1/(1+np.exp(-z))

    def _diff_sigmoid(self, z):
        return self._sigmoid(z)*(1-self._sigmoid(z))

    def _forward_prop(self, X_input):
        # layer 1
        self.net1 = (X_input-5)

        # layer 2
        self.net2 = np.dot(self.net1, self.w1_2)
        self.net2 = np.float64(self.net2)
        self.o2 = self._sigmoid(self.net2)

        # layer 3
        self.net3 = np.dot(self.o2, self.w2_3)
        self.net3 = np.float64(self.net3)
        self.o3 = self._sigmoid(self.net3)

    def _backward_prop(self, y):
        predict = self.o3 
        delta = predict - y
        # layer 3
        self.delta3 = np.multiply(delta, self._diff_sigmoid(self.net3))
#        self.delta3 = delta
        # layer 2
        self.delta2 = np.multiply(np.dot(self.delta3, self.w2_3.T), self._diff_sigmoid(self.net2))

        # create gradient
        m = self.net1.shape[0]
        self.w1_2_grad = np.dot(self.net1.T, self.delta2)/m
        self.w2_3_grad = np.dot(self.net2.T, self.delta3)/m


    def _update(self, learning_rate=0.5):
        self.w1_2 = self.w1_2 - learning_rate*self.w1_2_grad
        self.w2_3 = self.w2_3 - learning_rate*self.w2_3_grad

    def train(self, X, y, iteration):
        for i in range(iteration):
            self._forward_prop(X)
            self._backward_prop(y)
            self._update()


    def predict(self, X):
        self._forward_prop(X)
        y_pred = self.o3
        result_pred = []
        for i in range(len(y_pred)):
            result_pred.append(np.argmax(y_pred[i], axis=0))

        result_pred = np.array(result_pred)
        result_pred = np.reshape(result_pred, (-1, 1))
        return result_pred

    def accuracy(self, predict, y):
        cnt = np.sum(predict==y)
        return (cnt/len(y))*100




def main():

    # import the data
    iris_datasets = ds.load_iris()
    iris_data = iris_datasets.data
    iris_result = np.reshape(iris_datasets.target, (-1, 1))
    print("size of the iris datasets")
    print(len(iris_result))
    datasets = np.concatenate((iris_data, iris_result), axis=1)

    # shuffle the data
    np.random.shuffle(datasets)
    train_size = 100
    train_X, train_y = datasets[:train_size, 0:4], datasets[:train_size, 4:5]
    train_y = iris_classification(train_y)

    test_size = 50
    test_X, test_y = datasets[train_size:train_size+test_size, 0:4], datasets[train_size:train_size+test_size, 4:5]
    test_y_o = test_y
    test_y = iris_classification(test_y)



    # training
    testNN = NN()
    iteration = 150
    iteration = 1000
    testNN.train(train_X, train_y, iteration)

    # predict 
    predict_y = testNN.predict(test_X)
    print(testNN.o3)
    print("predict_y")
    print(predict_y)
    print("test_y")
    print(test_y_o)
    print("accuracy")
    print(testNN.accuracy(predict_y, test_y_o))


if __name__ == "__main__":
    main()






