# Load libraries
import pandas as pd
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

# Load dataset
dataset = pd.DataFrame({
    "teacherID": [1, 2, 3, 4],
    #"teacherName": ["Thomas", "Rom", "Eric", "Jeffrey"]
    "teacherAge": [33, 22, 55, 66]
    })

dataset2 = pd.DataFrame({
    "teacherID": [1, 2, 3, 4],
    #"teacherName": ["Thomas", "Rom", "Eric", "Jeffrey"]
    "teacherAge": [33, 22, 55, 66],
    "teacherHeight": [180, 170, 160, 190]
    })

dataset.hist()
print("-"*50)

pyplot.show()


