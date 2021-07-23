import numpy as np
from sklearn.svm import  SVC
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
x = np.array([[0,0],[1,1],[0,1],[1,0]])
y = [0,0,1,1] # 0이 파랑, 1이 빨강
xorSVM = SVC()
xorSVM.fit(x,y)

test_data = np.array([[0.8, 0.8],[0, 0.9]])
xorSVM.predict(test_data)

np.random.seed(0)
x = np.random.randn(300, 2)
y = np.logical_xor(x[:, 0] > 0, x[:, 1] > 0)
xorSVM.fit(x, y)

test_data = np.array([[0.8, 0.8],[0.2, 0.9]])
xorSVM.predict(test_data)

xx,yy = np.meshgrid(np.linspace(-3,3,500), np.linspace(-3,3,500))
z = xorSVM.decision_function(np.c_[xx.ravel(),yy.ravel()])
z = z.reshape(xx.shape)
plt.imshow(z, interpolation="nearest", extent=(xx.min(), xx.max(),
                yy.min(), yy.max()), aspect='auto', origin='lower',
                cmap=plt.cm.PuOr_r)
contours = plt.contour(xx, yy, z, levels=[0], lw=2, lt='--')
# contours = plt.contour(xx, yy, z, levels=[0], linewidths=2, linetypes='--')

plt.scatter(x[:, 0], x[:, 1], s=30, c=y,cmap=plt.cm.Paired)
plt.xticks(())
plt.yticks(())
plt.axis([-3, 3, -3, 3])
plt.show()





