#자전거 이동량 분석
from datetime import datetime
# import pandas_datareader.data as web
#pip install pandas_datareader
import numpy as np
import pandas as pd
import seaborn
from dateutil import parser
from matplotlib import pyplot as plt

# today = datetime(year=2021, month=7, day=1); print(today)
# lastDay = datetime(year=2021, month=1, day=1)
# print("{}일".format(today - lastDay))
# date1 = parser.parse("15th of Nov, 2021")
# date2 = parser.parse("2013-2-8")
# print(date1,"\t", date2)
# print(date1.strftime('%A'))
# date = np.array("2021-07-01", dtype=np.datetime64)
# # date = np.datetime64('2021-11-15 12:00:30')
#
# print(date)
# dateArray = date + np.arange(10) #10개짜리 날짜 배열
# print(dateArray)
# #
# index = pd.DatetimeIndex(['2017-10-12', '2017-11-12',
#  '2018-10-12', '2018-11-12'])
# data = pd.Series([0, 1, 2, 3], index=index)
# print(data['2017-11-1':'2018-10-31'])
#
# index = pd.DatetimeIndex(dateArray)
# data = pd.Series(np.arange(10), index=index)
# #data.index = index
# print(data)
#
# # 위 data에서 2021년은 며칠인지,
# # 데이터 5는 몇일자 데이터인지 출력
# print("2021년 남은 날짜는 {}일".format(len(data['2021'])))
# for key, value in data.items():
#     if(value == 5):
#         print("값 {}는 {}일자 데이터임".format(value,key))
#         break
#
#
# start = datetime(2016, 2, 19)
# end = datetime(2016, 3, 4)
# gs = web.DataReader("005930", "naver")#, start, end)
# # gs = web.get_data_yahoo('078930.KS')
#
# print(gs.head())
# gs.info()
# # plt.plot(gs['Close'])
# # plt.show()
# print(gs.index)

# plt.plot(gs['Close'],gs.index)
# plt.show()
#pd.read_csv()
# 파일이 있는 곳의 절대 경로 : 윈도우탐색기에서 FremontBridge.csv파일이 존재하는 곳을 찾아
# 주소줄을 복사해서 붙이고 \ -> \\로 바꿔 주시면 됩니다.
# data = pd.read_csv("FremontBridge.csv",
#                    index_col = 'Date', parse_dates=True)
# print(data.head())
# data.columns = ['East','West']
# data['Total'] = data.eval('West+East')
# print(data.head(5))
# print(data.describe())
# seaborn.set()
# # data.plot()
# # plt.ylabel("count of bicycle/hour")
# # plt.show()
# # weekly = data.resample('W').sum()
# # print(weekly)
# # weekly.plot(style=[':', '--', '-']) # East West Total 순서임
# # plt.ylabel("count of bicycle/week")
# # plt.show()
# # 30일 이동 평균(rolling)
# daily = data.resample('D').sum()
# daily.rolling(30, center=True).sum().plot(style=[':','--','-'])
# plt.ylabel('mean hourly count')
#
# # 가우스평활(Gaussian smoothing) 적용
# # 가우스 윈도우(Gaussian window) 같은 윈도우 함수를 사용해 롤링 평균을 부드럽게 표현
# # 윈도우 폭(50일)과 윈도우내 가우스 폭(10) 지정
# daily.rolling(50, center=True,
#  win_type='gaussian').sum(std=10).plot(style=[':','--','-'])
#
# # 하루의 시간대를 기준으로 한 함수로 평균 통행량을 보고 싶을때
# by_time = data.groupby(data.index.time).mean()
# hourly_ticks = 4*60*60*np.arange(6)
# by_time.plot(xticks=hourly_ticks, style=[':','--','-'])
# #
# # # 아침 8시, 저녁 5시 무렵에 많이 사용
# # # 동서가 확연하게 나누어짐.. 출근 사용량
# # # 요일별 통행량은?
# by_weekday = data.groupby(data.index.dayofweek).mean()
# by_weekday.index = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
# by_weekday.plot(style=[':','--','-'])
# #
# # # 주중과 주말의 시간대별 추이
# # # 데이터를 주말을 표시하는 플래그와 시간대별로 분류
# weekend = np.where(data.index.weekday <5, 'Weekday', 'Weekend')
# by_time = data.groupby([weekend, data.index.time]).mean()
#
# # 다중 서브플롯
# import matplotlib.pyplot as plt
# fgs, ax = plt.subplots(1, 2, figsize=(14,5))
# by_time.loc['Weekday'].plot(ax=ax[0], title='Weekdays', xticks=hourly_ticks, style=[':','--','-'])
# by_time.loc['Weekend'].plot(ax=ax[1], title='Weekends', xticks=hourly_ticks, style=[':','--','-'])
# #plt.show()

# 주중에서 양봉형태.. 주말에는 낮시간에 피크..
# 출퇴근 패턴에 영향을 미치는 날씨와 기온, 연중 시기등 기타 요인 분석이 필요

# 데이터를 적재하고 날짜를 인덱스로 지정
# FremontBridge.csv --> goo.gl/o3FkTM
# BicycleWeather.csv -> goo.gl/7ncbCd
counts = pd.read_csv("FremontBridge.csv", index_col='Date', parse_dates=True)
weather = pd.read_csv('BicycleWeather.csv', index_col='DATE', parse_dates=True)

print(counts.head(3))
print(weather.head(3))

# 일별 총 자전거 통행량을 계산해서 별도의 DataFrame에 넣음
daily = counts.resample('d').sum()
daily['Total'] = daily.sum(axis=1)
#daily['Total'] = daily["Fremont Bridge West Sidewalk"]
daily = daily[['Total']] # 다른 열 삭제

# 요일을 나타내는 열 추가
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i in range(7):
 daily[days[i]] = (daily.index.dayofweek == i).astype(float)

# print(daily.head(7))
# 휴일에 자전거를 타는 사람
from pandas.tseries.holiday import USFederalHolidayCalendar

cal = USFederalHolidayCalendar()
holidays = cal.holidays('2012', '2016')
daily = daily.join(pd.Series(1, index=holidays, name='holiday'))
daily['holiday'].fillna(0, inplace=True)
print(daily.head())
print(daily['2013-7-1':'2013-8-1'])