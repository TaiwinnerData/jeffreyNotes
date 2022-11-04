# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
import numpy as np

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

print(type(dataset))
array = dataset.values
x = array[:, 0:4]
y = array[:, 4]

print(x)
print(y)
print("-"*1000)
print(np.unique(y))


#print(type(array))
#print(array)
