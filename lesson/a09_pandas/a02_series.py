'''
Created on 2017-07-27 12:50

@ product name : PyCharm Community Edition

@ author : yoda
'''
from mymod.print import *
import numpy as np
import pandas as pd

goods = pd.Series([4000, 3000, 5000, 2500], index=["apple", "orange", "grape", "melon"])
print(goods)

# 3000원 이상 가격 보기
print(goods[goods>3000])

goods2 = goods + 300
print(goods2)

# 총계
print(np.sum(goods2))

# Series 만들기 2 (using dict)
# 1. key
# 2. value
# 3. dict  dict(zip(key, value))
# 2. Series에 할당

keys = ["일식", "한식", "중식", "편의점"]
values = [3000, 4000, 5000, 1500]
dic = dict(zip(keys, values))
print(dic)
launch = pd.Series(dic)
print(launch)
launch.name = "점심시간"
launch.index.name = "메뉴"
print(launch)