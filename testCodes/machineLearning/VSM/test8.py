# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from matplotlib import pyplot as plt


# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
print("show the original dataset:")
print(dataset)
print(dataset.values)
scatter_matrix(dataset)
plt.show()


"""

# Split dataset
iris_data = dataset.values
x = iris_data[:, 0:4]
y = iris_data[:, 4]


print("Show the whole data:")
print(x)
print(y)
print("show the train data"*100)


train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.20)
print("show the train data")
print(train_x, train_y)
print("show the result data"*100)

# ---------------------
# with train_test_split function then you don't need the scripts below which is also for separation
#train_x = x[0:100]
#train_y = y[0:100]

#test_x = x[100:150]
#test_y = y[100:150]
# ---------------------




# create model
model = SVC(kernel='linear', C=1.0)
model.fit(train_x, train_y)


# fit the test data
print("Show the prediction result")
print(model.predict(test_x))


# plot the diagram result
plt.scatter(test_x, test_y)

plt.show()
"""
