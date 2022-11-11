# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# Show the 'shape' which is the columns number and rows number
print(dataset.shape)
print("-"*50)
# Show the 'head' of the dataframe which is first few rows of the Dataframe.
print(dataset.head(20))
print("-"*50)
# Show descriptions
print(dataset.describe())
print("-"*50)
# Class distribution
print(dataset.groupby('class').size())
print("-"*50)
# box and whisker plots
#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# histograms
#dataset.hist()
print("-"*50)
# scatter plot matrix
scatter_matrix(dataset)     # If you don't set the color, the dots default color would be blue.
scatter_matrix(dataset, color='red')     # you can set the color for all kinda class of dot. If you want to set different color to different class, you the set below.
scatter_matrix(dataset, color=['red', 'blue'])     # If you want to set different color for different class dot, you can use....... Fuck! this doesn't work! this should work on all the data which is not what i want.
# here's a refernece talk about this: 
# https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset


print("-"*50)

pyplot.show()

# split-out validation dataset
array = dataset.values
x = array[:, 0:4]
y = array[:, 4]

# show the value of the dataset.
print("-"*50)
print("show dataset values")
print(dataset.values)
print("length of the dataset")
print(len(dataset.values))
print("-"*50)
print("x")
print(x)
print("length of x")
print(len(x))
print("-"*50)
print("y")
print(y)

x_train, x_validation, y_train, y_validation = train_test_split(x, y, test_size=0.20, random_state=1)
print("x_train")
print(x_train)
print("length of x_train")
print(len(x_train))
print("-"*50)
print("x_validation")
print(x_validation)
#print("-"*50)
#print("y_train")
#print(y_train)
#print("-"*50)
#print("y_validation")
#print(y_validation)

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# Evaluate each model in turn 
results = []
names = []


print("#"*300)
print("show the models")
print(models)

print("#"*300)
print("show the algorithm models")
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, x_train, y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))




