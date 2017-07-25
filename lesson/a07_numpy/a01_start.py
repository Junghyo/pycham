'''
Created on 2017-07-25 09:58

@ product name : PyCharm Community Edition

@ author : yoda
'''

import datetime

import numpy as np

# from basic_numpy import * (권장하지 않음)


# li = range(1, 10)
# s = datetime.datetime.now()
# print("list 작업 시간 :", s)
#
# for cnt in li:
#     cnt = cnt * 10
#
# s = datetime.datetime.now()
# print("list 종료시간 :". s)

# ndarray로 처리
ar = np.arange(1, 1000000)

s = datetime.datetime.now()
print("ndarray 작업시작 시간 :", s)
ar = ar * 10

s = datetime.datetime.now()

print("ndarray 작업종료 시간 :", s)
