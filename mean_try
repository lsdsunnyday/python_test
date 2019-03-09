import re
import sys

import numpy as np
import pandas as pd


xlsx = pd.read_excel('站点2018年1月1日-12月31日小时均值.xls','站点小时数据')
xlsx['month']=pd.to_datetime(xlsx['时间']).dt.month
xlsx['day']=pd.to_datetime(xlsx['时间']).dt.day
xlsx['hour']=pd.to_datetime(xlsx['时间']).dt.hour

xlsx.drop(['城市名称','区县名称','站点名称','时间'],axis=1,inplace=True)
xlsx.drop([0,], inplace=True)

xlsx = xlsx.set_index([xlsx['month'],xlsx['day'],xlsx['hour']])
xlsx.drop(['month','day','hour'],axis=1,inplace=True)

#处理之前先切片
xlsx = xlsx.sort_index(level=0)


mon_data = xlsx.mean(level=0)

year_data = xlsx.mean()

day_data = xlsx.mean(level=[0,1])

hour_data = xlsx.mean(level=[0,2])

#春夏秋季小时平均
hour_data.loc[(slice(3,5), slice(None)), :].mean(level=1)
hour_data.loc[(slice(6,8), slice(None)), :].mean(level=1)
hour_data.loc[(slice(9,11), slice(None)), :].mean(level=1)
