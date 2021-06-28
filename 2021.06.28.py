import pandas as pd
import numpy as np

print(pd.__version__)

# Series : 라벨이 붙은 1차원 배열 (데이터 라벨은 자료형을 설명함)
data = [1,2,3,4]
index = ["A","B","C","D"]
a = pd.Series(data=data, index=index)  # 키워드 인자
b = pd.Series(data, index)  # 위치 인자
print(a)
print(b)

# DataFrame : Series(컬럼명:데이터셋의 튜플)와 인덱스로 만든다
data = {"Column1":[1,2,3,4,], "Column2":['a', 'b', 'c', 'd']}
c = pd.DataFrame(data, index)
print(c)

# DataFrame : row(컬럼값들의 집합)와 컬럼명으로 만든다
data = [[1, "a", False], [2, "b", True],
        [3, "c", False], [4, "d", True]]
columns = ["Column1", "Column2", "Column3"]
d = pd.DataFrame(data, index, columns)
print(d)

# 실행결과
#    Column1 Column2  Column3
# A        1       a    False
# B        2       b     True
# C        3       c    False
# D        4       d     True

# DataFrame : 인덱스와 컬럼 모두 자동할당
f = pd.DataFrame(data)
print(f)


#numpy의 ndarray를 사용
# data = np.zeros((4,2))
# g = pd.DataFrame(data)
# print(g)

data = [
        ['Sun', 10, None],
        ['Mon', 0, None],
        ['Tue', 15, 'Childen\'s Day'],
        ['Wed', 3, None],
        ['Thur', 100, 'Birth day'],
        ['Fri', 200, "Parent's Day"],
        ['Sat', 7, None]
        ]
index = pd.date_range("20210502", periods=7)
column = ["Day", "Expenses", "Anniversary"]
print(pd.DataFrame(data=data, index=index, columns=column))

# 실행결과
#              Day  Expenses    Anniversary
# 2021-05-02   Sun        10           None
# 2021-05-03   Mon         0           None
# 2021-05-04   Tue        15  Childen's Day
# 2021-05-05   Wed         3           None
# 2021-05-06  Thur       100      Birth day
# 2021-05-07   Fri       200   Parent's Day
# 2021-05-08   Sat         7           None



# pandas의 read_() 함수를 이용해 다양한 데이터 포맷을 불러올 수 있다.
file = "C:/Users/hyesu/Downloads/train.csv"
df = pd.read_csv(file)
print(df)