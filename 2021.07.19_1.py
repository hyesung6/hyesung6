import numpy as np
from sklearn import  svm

x = np.array([[0,0],[1,1]])
y = [0, 1]
lSVM = svm.LinearSVC()
lSVM.fit(x, y)

lSVM.set_params(penalty='10')
yPred = lSVM.predict([[0.6, 0.1]])
# yPred = lSVM.predict([[0.4, 0.4]])
print(yPred)

score = lSVM.score(x, y)
print("정확도: ", score)
coefficient = lSVM.coef_
intercept = lSVM.intercept_
print("계수 : \n", coefficient)
print()
print("절편 : \n", intercept)

import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

coefficient = lSVM.coef_[0]
intercept = lSVM.intercept_[0]
print("계수 : \n", coefficient)

slope = -coefficient[0] / coefficient[1]
xx = np.linspace(0,1,5)
yy = slope * xx - intercept / coefficient[1]

h0 = plt.plot(xx, yy, 'k-', label="Hyperplane")

plt.scatter(x[:, 0], x[:, 1], c = y)
plt.legend()
plt.show()