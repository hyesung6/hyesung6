# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10xmVBL2y9fhM9I3t61YBFgowFcm8bEhk
"""

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

data = load_boston()
xTrain, xTest, yTrain, yTest\
    = train_test_split(data.data, data.target, random_state=42)
data.feature_names

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(xTrain, yTrain)

score = model.score(xTest, yTest)
print("정확도: ", score)

coefficient = model.coef_
intercept = model.intercept_
print("계수 : \n", coefficient)
print()
print("절편 : \n", intercept)

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

data = load_diabetes()
xTrain, xTest, yTrain, yTest\
    = train_test_split(data.data, data.target, random_state=42)
print(data, "\n", data.target.size)

from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)
ridge.fit(xTrain, yTrain)

score = ridge.score(xTest, yTest)
print("정확도: ", score)

from sklearn.linear_model import Lasso

lasso = Lasso(alpha=1.0)
lasso.fit(xTrain, yTrain)

score = lasso.score(xTest, yTest)
print("정확도: ", score)

from sklearn.linear_model import ElasticNet

elastic = ElasticNet(alpha=1.0, l1_ratio=0.5)
elastic.fit(xTrain, yTrain)

score = elastic.score(xTest, yTest)
print("정확도: ", score)

from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

linear = LinearRegression()
linear.fit(xTrain, yTrain)

score = linear.score(xTest, yTest)
print("정확도: ", score)


coefficients = np.vstack((linear.coef_, ridge.coef_, lasso.coef_, elastic.coef_))
index = ["linear", "ridge", "lasso", "elastic"]
coefficients_df = pd.DataFrame(coefficients, columns=data.feature_names, index=index)

print("정규화 선형회귀 모델별 가중치(계수) 비교")
coefficients_df

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

dataset = load_iris()
data = pd.DataFrame(dataset.data, columns=dataset.feature_names)
xTrain, xTest, yTrain, yTest = train_test_split(data, dataset.target, random_state=42)

import matplotlib.pyplot as plt

xTrain.plot(kind="box")
plt.title("xTrain")
plt.show()
xTest.plot(kind="box")
plt.title("xTest")
plt.show()

from sklearn.preprocessing import MinMaxScaler

mms = MinMaxScaler()
xTrainScaled = mms.fit_transform(xTrain)
xTestScaled = mms.fit_transform(xTest)
xTestScaled

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors = 5)
model.fit(xTrainScaled, yTrain)

from sklearn.metrics import accuracy_score

pred = model.predict(xTestScaled)
accuracy_score(yTest, pred)

from sklearn.datasets import load_breast_cancer
import pandas as pd

dataset = load_breast_cancer()
train = pd.DataFrame(dataset.data, columns=dataset.feature_names)
target = pd.DataFrame(dataset.target, columns=["cancer"])
data = pd.concat([train, target], axis=1)
data.info()

xTrain, xTest, yTrain, yTest = train_test_split(
    data[["mean radius"]], data[["cancer"]], random_state=42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver="liblinear")
model.fit(xTrain, yTrain)

pred = model.predict(xTest)
acc = accuracy_score(yTest, pred)
print("mean radius 만으로 예측한 결과:{}\n".format(acc), pred)

from seaborn import lmplot
import matplotlib.pyplot as plt

lmplot(x="mean radius", y="cancer", data=data, logistic=True)
plt.show()

xTrain, xTest, yTrain, yTest = train_test_split(data.loc[:,:"cancer"], 
                                                data.loc[:,"cancer"], 
                                                random_state=42)
model.fit(xTrain, yTrain)
yPred = model.predict(xTest)
score = model.score(xTest, yTest)

print(f"전체 데이터로 예측한 결과: {score}")

################################
import seaborn as sns

data = sns.load_dataset("titanic")
data.head()

predData = data.drop(columns=["alive", "who", "adult_male", "class", "embark_town"])
predData.drop("deck", axis = 1, inplace=True)
predData.head()

#p. 338페이지부터...