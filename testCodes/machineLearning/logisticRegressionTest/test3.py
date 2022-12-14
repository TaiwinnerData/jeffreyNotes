# Linear Support Vector Machine Model Test
# Load libraries
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)


# Split dataset
array = dataset.values
x = array[:, 0:4]
y = array[:, 4]
print(x)
print(y)


x_train, x_validation, y_train, y_validation = train_test_split(x, y, test_size=0.20, random_state=1)
print(x_train)
print(y_train)

# test
model = LogisticRegression()
model.fit(x_train, y_train)
print(model)
print(model.fit(x_train, y_train))
