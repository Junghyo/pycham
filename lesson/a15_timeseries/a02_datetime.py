'''
Created on 2017-08-02 20:46

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

import datetime, time
dt = datetime.datetime.now()
print("날짜:",dt.date(),"\t시간:",dt.time())

d = datetime.datetime(2017,9,7)
print("datetime:", d)

d = datetime.date(2017,9,7)
print("date:", d)

t = datetime.time(18, 30, 1)
print("time:", t)

# combine : 날짜 + 시간
print("combine:", datetime.datetime.combine(d, t))

print("start!!!")
print(datetime.datetime.now())
## time.sleep(초단위) : 해당 시간 동안 처리를 중지
time.sleep(10)
print("finish!!!")
print(datetime.datetime.now())

## parse() : 문자열 ==> datetime 형식으로 변경..
from dateutil.parser import parse
str = "2017-08-02"
print(str)  # 2017-08-02
print(type(str))    # <class 'str'>
print(parse(str))   # 2017-08-02 00:00:00
print(type(parse(str))) # <class 'datetime.datetime'>