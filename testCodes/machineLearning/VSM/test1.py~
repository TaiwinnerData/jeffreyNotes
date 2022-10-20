import numpy as np
import pandas as pd
import cvxopt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plot
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix


# Load dataset
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
#dataset = pd.read_csv(url, namees = names)

x, y = make_blobs(n_sample=250, centers=2, random_state=0, cluster_std=0.60)

# Split dataset
array = dataset.values
x = array[:, 0:4]
y = array[:, 4]


# Create model
x_train, x_validation, y_trian, y_validation = train_test_split(x, y, test_size=0.20, random_state=1)
print(x_train)
print(y_train)
svm = SVM()
svm.fit(x_train, y_train)

plt.scatter(x_train[:, 0], x_train[: 1], c=y_train, cmap='winter')
ax = plt.gca()
xlim = ax.get_xlim()
w = svc.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(xlim[0], xlim[1])

yy = a * xx - svc.intercept_[0] / w[1]
plt.plot(xx, yy)
yy = a * xx - (svc.intercept_[0] - 1) / w[1]
plt.plot(xx, yy, 'k--')
yy = a * xx - (svc.intercept_[0] + 1) / w[1]
plt.plot(xx, yy, 'k--')
