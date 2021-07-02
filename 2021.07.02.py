import pandas as pd
import numpy as np
from datetime import datetime
import pandas_datareader.data as web      #pip install pandas_datareader
import seaborn
from dateutil import parser
from matplotlib import pyplot as plt

today = datetime(year=2021, month=7, day=1); print(today)
lastDay = datetime(year=2021, month=1, day=1)
print("{}일".format(today - lastDay))
date1 = parser.parse("15th of Nov, 2020")
date2 = parser.parse("2013-2-8")
print(date1, "\t", date2)
print(date1.strftime('%A'))
date = np.array("2021-07-01", dtype=np.datetime64)
# date = np.datetime64('2021-12-25 12:00:30')

print(date)
dateArray = date + np.arange(10) #10개 날짜 배열
print(dateArray)

index = pd.DatetimeIndex(['2017-10-12', '2017-11-12', '2018-10-12', '2018-11-12'])
data5 = pd.Series([0, 1, 2, 3], index=index)
print(data5['2017-10-12':'2018-10-31'])

index = pd.DatetimeIndex(dateArray)
data = pd.Series(np.arange(10), index=index)
# data.index = index
print(data)
# 위 data에서 2021년은 며칠인지, 데이터 5는 며칠자 데이터인지 출력

print("2021년 남은 날짜는 {}일".format(len(data['2021'])))
for key, value in data.items():
    if(value == 5):
        print("값 {}는 {}일자 데이터임".format(value, key))
        break
# ------ 이어서


# start = datetime(2016, 2, 19)
# end = datetime(2016, 3, 4)
# gs = web.DataReader("078930.KS", "naver", start, end)
# # gs = web.get_data_yahoo('005930.KS')
# print(gs.head())
#

data =  pd.read_csv("C:\\Users\\hyesu\\PycharmProjects\\pythonProject\\FremontBridge.csv",
                    index_col = 'Date', parse_dates=True)
print(data.head())
data.columns = ['East', 'West']
data['Total'] = data.eval('West+East')
print(data.head(5))
print(data.describe())
seaborn.set()
data.plot()
plt.ylabel("count of bicycle/hour")
# plt.show()
weekly = data.resample('W').sum()
print(weekly)
weekly.plot(style=[':', '--', '-'])
plt.ylabel("count of bicycle/week")
# plt.show()


# 30일 이동 평균(rolling)
daily = data.resample('D').sum()
daily.rolling(30, center=True).sum().plot(style=[':', '--', '-'])
plt.ylabel('mean hourly count')
# plt.show()

# 가우스평활(Gaussian smoothing) 적용
# 가우스 윈도우 같은 윈도우 함수를 사용해 롤링 평균을 부드럽게 표현
# 윈도우 폭(50일)과 윈도우 내 가우스 폭 (10) 지정
daily.rolling(50, center=True, win_type='gaussian').sum(std=10).plot(style=[':', '--', '-'])


# 하루의 시간대를 기준으로 한 함수로 평균 통행량을 보고 싶을 때
by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4*60*60*np.arange(6)
by_time.plot(xticks=hourly_ticks, style=[':', '--', '-'])


# 아침 8시, 저녁 5시 무렵에 많이 사용
# 동서가 확연하게 나누어짐.. 출근 사용량
# 요일별 통행량은?
by_weekday = data.groupby(data.index.dayofweek).mean()
by_weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
by_weekday.plot(style=[':', '--', '-'])


# 주중과 주말의 시간대별 추이
# 데이터를 주말을 표시하는 플래그와 시간대별로 분류
weekend = np.where(data.index.weekday <5, 'Weekday', 'Weekend')
by_time = data.groupby([weekend, data.index.time]).mean()

# print(len(data))
