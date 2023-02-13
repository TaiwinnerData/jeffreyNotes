import numpy as np
import pandas as pd



# Create neural network object class by using backward propagation.
class NN(object):
    def __init__(self):
        self.feature_number = 2  # feature numbers
        self.output_number = 1 # class number
        self.hidden_number = 2 # only single layer with 6 units

        # initilization matrix of weights In this case we have 2 layers of weights
        np.random.seed(1)
        self.w1 = np.random.randn(self.feature_number, self.hidden_number) # first layer's weights
        self.w2 = np.random.randn(self.hidden_number, self.output_number) # second layer's weights

    def _forward_propagation(self, X): # X is the data input
        # layer 1
        self.net1 = np.dot(self.w1.T, X.T)
        self.net1 = np.float64(self.net1) # change the data type to numpy's float or the _simgoid can't read it.
        self.o1 = self._sigmoid(self.net1)
        
        # layer 2
        self.net2 = np.dot(self.w2.T, self.o1)
        self.net2 = np.float64(self.net2)
        self.o2 = self._sigmoid(self.o3)

    def _sigmoid(self, z):
        return 1/(1+np.exp(-z))

    def _diff_sigmoid(self, z):
        return self._sigmoid(z)*(1-self._sigmoid(z))

    def _backward_propagation(self, X, y):
        predict = self.o3
        delta3 = predict - y
        self.dz3 = np.multiply(delta3, self._diff_sigmoid(self.net2))



# import example data, for this test I use weight-height datasets.
data_number = 2
datasets = pd.read_csv("weight-height.csv")
datasets = pd.DataFrame.to_numpy(datasets)
datasets, data_result = datasets[:data_number, 1:3], datasets[:data_number, 0:1]

# turn all the y value to 1 or 0
for i in range(len(data_result)):
    if data_result[i] == "Male":
        data_result[i] = 1
    else:
        data_result[i] = 0


def main():
    testNN = NN()
    testNN._forward_propagation(datasets)
    print("show weight before back propagation")
    print("weight1")
    print(testNN.w1)
    print("weight2")
    print(testNN.w2)
    testNN._backward_propagation(datasets, data_result)
    print("show testNN.a3")
    print(testNN.a3)
    print("show testNN.dz3")
    print(testNN.dz3)
    print("weight1")
    print(testNN.w1)
    print("weight2")
    print(testNN.w2)





if __name__ == "__main__":
    main()
