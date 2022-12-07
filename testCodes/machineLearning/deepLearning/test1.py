from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target

print('A data:', X[0], 'nLabel:', y[0])
'''output
A data:[5.1 3.5 1.4 0.2]
Label: 0
'''

import numpy as np
re_y = np.array([1 if i==0 else 0 for i in y]) # relabel, 'setosa':1, 'not setosa':0
print(re_y)
'''output
[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0]
'''


import matplotlib.pyplot as plt

def plot(xfeature_name, yfeature_name, xfeature, yfeature, ori_label, re_label):
    # setting color
    ori_color = {0: 'red', 1: 'blue', 2: 'yellow'} # label, 0:'setosa' 1:'versicolor' 2:'virginica'
    relbl_color = {0: 'blue', 1: 'red'} # relabel, 0:'not setosa' 1:'setosa'
    # plot oringinal label figure
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.subplots_adjust(wspace = 0.5)
    plt.title("Original Label")
    plt.xlabel(xfeature_name)
    plt.ylabel(yfeature_name)
    for i, j, color in zip(xfeature, yfeature, ori_label):
        plt.scatter(i, j, c=ori_color[color], marker='o', s=50, edgecolor='k',cmap=plt.cm.Spectral)
    # plot relabel figure
    plt.subplot(1, 2, 2)
    plt.title("Relabel")
    plt.xlabel(xfeature_name)
    plt.ylabel(yfeature_name)
    for i, j, color in zip(xfeature, yfeature, re_label):
        plt.scatter(i, j, c=relbl_color[color], marker='o', s=50, edgecolor='k',cmap=plt.cm.Spectral)

plot('sepal length(cm)', 'sepal width(cm)', X[:, 0], X[:, 1], y, re_y)
plot('petal length(cm)', 'petal width(cm)', X[:, 2], X[:, 3], y, re_y)
plt.show()
