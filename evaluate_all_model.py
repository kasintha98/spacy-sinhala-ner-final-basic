import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
iris.data.shape, iris.target.shape((150, 4), (150,))

clf = svm.SVC(kernel='linear', C=1)
scores = cross_validation.cross_val_score(
clf, iris.data, iris.target, cv=5)

print(scores)