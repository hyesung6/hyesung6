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

def hours_of_daylight(date, axis=23.44, latitude=47.61):
     # 해당 날짜의 일조시간 계산
     days = (date - pd.datetime(2000, 12, 21)).days
     m = (1. -np.tan(np.radians(latitude))
     * np.tan(np.radians(axis) * np.cos(days * 2 * np.pi / 365.25)))
     return 24 * np.degrees(np.arccos(1 - np.clip(m, 0, 2))) / 180.
daily['daylight_hrs'] = list(map(hours_of_daylight, daily.index))

daily[['daylight_hrs']].plot()
plt.ylim(8, 17)

# 데이터에 평균 기온과 전체 강수량 추가
# 인치 단위의 강수량과 더불어 날이 건조했는지(강수량이 0) 알려주는 플래그 추가
# 기온은 섭씨 1/10도 단위, 섭씨 1도 단위로 변환
weather['TMIN'] /= 10
weather['TMAX'] /= 10
weather['Temp (c)'] = 0.5 * (weather['TMIN'] + weather['TMAX'])

# 강수량은 1/10mm 단위; 인치 단위로 변환
weather['PRCP'] /= 254
weather['dry day'] = (weather['PRCP'] == 0).astype(int)
daily = daily.join(weather[['PRCP', 'Temp (c)', 'dry day']])
print(daily.head(3))

# 첫날 부터 증가하는 계수기를 추가해 몇 해가 지났는지를 측정
# 관측된 일별 통행량이 연도별로 증가하거나 감소하는지를 측정
daily['annual'] = (daily.index - daily.index[0]).days / 365.
#print(np.sum(daily['2013-8-1':'2013-8-5']))#7967
#print(np.sum(daily['2014-8-1':'2014-8-5']))#9209
#print(np.sum(daily['2015-8-1':'2015-8-5']))#8428
#print(np.sum(daily['2016-8-1':'2016-8-5']))#9770
#print(np.sum(daily['2017-8-1':'2017-8-5']))#8213
#print(np.sum(daily['2018-8-1':'2018-8-5']))#7270
print("NaN data\n", daily.tail(3))
# 널값 행은 제거
daily.dropna(axis=0, how='any', inplace=True)
column_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun',
 'holiday', 'daylight_hrs', 'PRCP', 'dry day','Temp (c)', 'annual']
print("NaN record removed\n", daily.tail(10))

X = daily[column_names] # label data
y = daily['Total'] # solution

# pip install sklearn
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=False)
model.fit(X, y) # 기존 데이터를 학습함
daily['predicted'] = model.predict(X) # 결과 예측
#총 자전거 통행량과 예상 자전거 통행량 비교
daily[['Total', 'predicted']].plot(alpha=0.5) # 예측값과 실제 결과값을 그래프로 그림
plt.show()

# 여름에 차이가 많이 남
# 고려한 요인 외
## -. 사람들이 일하러 갈때 자전거를 탈지 결정하는 데 영향을 주는 요인은 뭐가 있을까?
# 미처 고려하지 못한 비선형 관계
## -. 사람들이 기온이 너무 높거나 낮을 때 자전거를 덜 탈 수 도 있다.

# 각 특징이 요일별 자전거 통행량에 얼마나 기여하는지 추정하는 선형 모델 계수
params = pd.Series(model.coef_, index=X.columns)
print(params)

# 불확실성에 대한 척도 없이는 해석이 어려움
# 데이터의 부트스트랩 표본 재추출(bootstrap resampling)을 사용하여 불확실성을 계산
from sklearn.utils import resample
np.random.seed(1)
err = np.std([model.fit(*resample(X, y)).coef_
 for i in range(1000)], 0 )

# 추정된 오차를 가지고 결과를
print(pd.DataFrame({'effect' : params.round(0), 'error' : err.round(0)}))