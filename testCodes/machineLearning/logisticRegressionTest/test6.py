from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_blobs
# generate 2d classification dataset
x, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)
print(x)
print(y)
# fit final model 
model = LogisticRegression()
model.fit(x, y)
