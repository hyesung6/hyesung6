import math

from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
#1. 학습데이터 마련 - 훈련용 데이터/검증용 데이터를 분리
#2. 모델을 선택
#3. fitting -> 모델에 학습데이터를 넣어서
# 입력값과 출력값으로 feature값을 fitting
#4. prediction -> 새로운 입력값을 넣어 결과를 예측
#5. validation -> 검증, 예측의 결과의 정확도(신뢰도)를 검사
# 검증용 데이터를 입력하여 예측된 결과가 실제 결과와 얼마나 일치하는지 확인

#1단계
iris = load_iris()
iris_data = iris.data
print("iris dataset Items : \n", iris.items())
print("특성의 이름: \n{}".format(iris['feature_names']))

# 열의 이름은 iris_dataset.feature_names에 있는 문자열을 사용합니다.
iris_data_pd = pd.DataFrame(iris_data, columns=iris.feature_names)
petals = pd.DataFrame(iris_data_pd.values[:,2:4],
                      columns=['petal length (cm)', 'petal width (cm)'])
plt.scatter(petals.values[:, 0], petals.values[:, 1])
# plt.show()

from sklearn.cluster import KMeans
plt.figure(figsize=(7,5))
km = KMeans(n_clusters=2, random_state=10)
km.fit(iris_data_pd.iloc[:,2:4])
y_pred = km.predict(iris_data_pd.iloc[:,2:4])
plt.scatter(iris_data_pd.iloc[:,2],iris_data_pd.iloc[:,3], c=y_pred)
plt.title("Clustering")
plt.xlabel("petal length")
plt.ylabel("petal width")
# plt.show()

print(y_pred)

print(iris_data_pd.iloc[96:101,2:4])

print("cluster 중심점 :", km.cluster_centers_)

def distance(x1, y1, x2, y2) :
    dx = x2 - x1
    dy = y2 - y1
    squared = dx**2 + dy**2
    result = math.sqrt(squared)
    return result

dis1 = distance(iris_data_pd.iloc[98,2],iris_data_pd.iloc[98,3],
                km.cluster_centers_[0][0], km.cluster_centers_[0][1])
dis2 = distance(iris_data_pd.iloc[98,2],iris_data_pd.iloc[98,3],
                km.cluster_centers_[1][0], km.cluster_centers_[1][1])

print("distance to cluster center0 : ", dis1)
print("distance to cluster center1 : ", dis2)

n_cluster = [3,4,6,12]
for n in n_cluster :
    count = 1
    km = KMeans(n_clusters=n, random_state=20)

    km.fit(iris_data_pd.iloc[:,2:4])
    y_pred = km.predict(iris_data_pd.iloc[:,2:4])

    plt.figure(count)
    plt.scatter(iris_data_pd.iloc[:,2],iris_data_pd.iloc[:,3], c=y_pred)
    plt.title("Clustering" + str(n))
    plt.xlabel("petal length")
    plt.ylabel("petal width")
    count += 1
    plt.show()
