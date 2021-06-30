import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False

# def n_square(x, n):
#     return x ** n
#
# print(df[["Age", "SibSp", "Fare"]])              #df는 DataFrame
# b = df[["Age", "SibSp", "Fare"]]).apply(n_square, args=[2])
# print(b)
#
# b.to_scv("AgeSibSpFare.scv")
#
# for c in dir(df) :
#     if c.startswith("to_") :

import matplotlib.font_manager as fm
fm.rcParams["font.family"] = "Malgun Gothic"

#Seaborn과 matplotlib의 차이점 : 씨본은 통계 모델 데이터가 있다

import seaborn as sns
sns.__version__

print(sns.get_dataset_names())        #데이터셋 모델 목록 출력

# d = sns.load_dataset("iris")
# print(d)

iris = sns.load_dataset("iris")
print(iris)

x = iris.petal_length.values
# x = iris.petal_width.values
# x = iris.sepal_length.values
# x = iris.sepal_width.values
# sns.rugplot(x=x)
# plt.title("Iris 데이터 중, 꽃잎의 길이에 대한...")
# plt.show()

# sns.kdeplot(x)
# plt.show()

# sns.distplot(x, kde=True, rug=True, hist=True)
# plt.title("Iris DataSet, petal length...")
# plt.show()

# titanic = sns.load_dataset("titanic")
# sns.countplot(x="class", data=titanic)
# plt.title("타이타닉 호")
# plt.show()

# sns.jointplot(x="sepal_length",  y="sepal_width", data=iris)
# plt.suptitle("sepal length and width... Joint Plot")
# plt.show()

# sns.jointplot(x="sepal_length",  y="sepal_width", data=iris, kind="kde")
# plt.suptitle("꽃받침의 길이와 넓이",
#              y=1.02
#              )
# plt.show()

sns.pairplot(iris, hue="species", markers=["o", "s", "D"])
plt.title("Iris Pair Plot, Hue로 꽃의 종을 시각화")
plt.show()


# p. 237