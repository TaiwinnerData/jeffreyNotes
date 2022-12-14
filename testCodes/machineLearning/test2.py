# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split

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
scatter_matrix(dataset)
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




