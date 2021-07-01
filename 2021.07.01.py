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
