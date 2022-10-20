# Load libraries
import pandas as pd
from matplotlib import pyplot

# Load dataset
dataset = pd.DataFrame({
    "teacherID": [1, 2, 3, 4],
    "teacherName": ["Peter", "Sandra", "Thomas", "Jeffrey"]
    })

# Show the 'shape' which is the columns number and rows number
print(dataset.shape)
# Show the 'head' of the dataframe which is first few rows of the Dataframe.
print(dataset.head(20))
# Show descriptions
print(dataset.describe())

