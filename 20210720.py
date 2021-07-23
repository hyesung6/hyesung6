import numpy as np
from sklearn import svm
import numpy as np
from sklearn.svm import  SVC
import matplotlib.pyplot as plt
from matplotlib import style

x = np.array([[0,0],[1,1],[0,1],[1,0]])
y = [0,0,1,1]
xorSVM = svm.SVC()
xorSVM.fit(x, y)

yPred = xorSVM.predict([[0.1, 0.2], [0.4, 0.4], [0.44, 0.44], [0.5, 0.5], [0.6, 0.7]])
print(yPred)
print("#######################################")
np.random.seed(0)
x = np.random.randn(300, 2)
y = np.logical_xor(x[:, 0] > 0, x[:, 1] > 0)
for a,b in zip(x, y) :
    print(a, "::", b)
print("------- Predict ------")
xorSVM.fit(x, y)
xPred = [[0.0000001, -0.000000002], [0.25, -0.3], [0.4, 0.4], [-0.44, -0.44], [-0.5, 0.5], [0.6, 0.7], [0.99999, -0.88888]]
yPred = xorSVM.predict(xPred)
print(yPred)
for a,b in zip(xPred, yPred) :
    print(a, "::", b)

xx, yy = np.meshgrid(np.linspace(-3,3,500),np.linspace(-3,3,500))

Z = xorSVM.decision_function(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           aspect='auto',origin='lower', cmap=plt.cm.PuOr_r)
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2,linetypes='--')
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Paired)
plt.xticks(())
plt.yticks(())

plt.axis([-3,3,-3,3])
plt.show()
