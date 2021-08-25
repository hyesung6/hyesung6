import numpy as np
from sklearn import  svm

x = np.array([[0,0],[1,1]])
y = [0, 1]
lSVM = svm.LinearSVC()
lSVM.fit(x, y)

lSVM.set_params(penalty='10')
yPred = lSVM.predict([[0.44, 0.43]])
print(yPred)