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
        self.w1_2 = np.random.randn(self.feature_number, self.hidden_number) # first layer's weights  2*2 matrix
        self.w2_3 = np.random.randn(self.hidden_number, self.output_number) # second layer's weights  2*1 matrix

    def _forward_propagation(self, X): # data input X
        # layer 1
        self.net1 = X
        self.net2 = np.dot(self.net1, self.w1_2)
        self.net2 = np.float64(self.net2) # change the data type to numpy's float or the _simgoid can't read it.
        print("show self.net2")
        print(self.net2)
        self.o2 = self._sigmoid(self.net2)
        print("show self.o2")
        print(self.o2)
        
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
        self.delta2 = np.dot(self.delta3, self.w2_3.T)
        print("show delta2")
        print(self.delta2)
        print(self.delta2.shape)



# import example data, for this test I use weight-height datasets.
data_number = 1 
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
    testNN._backward_propagation(data_result)






if __name__ == "__main__":
    main()
