'''
Created on 2017-07-28 15:44

@ product name : PyCharm Community Edition.

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

items = {
    "apple": {"count": 10, "price": 1500},
    "banana": {"count": 5, "price": 2000},
    "grape": {"count": 7, "price": 700},
    "orange": {"count": 8, "price": 500},
    "pineapple": {"count": 13, "price": 600},
    "kiwi": {"count": 3, "price": 2500},
    "mango": {"count": 17, "price": 3000},
    "lemon": {"count": 10, "price": 1200},
}

df = pd.DataFrame(items)
dft = df.T
print(dft)
dft.to_csv("z01_fruit.csv", index=False, header=False)