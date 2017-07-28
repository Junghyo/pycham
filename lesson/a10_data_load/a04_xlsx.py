'''
Created on 2017-07-28 15:53

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import csv

# sheetname=: sheet 지정
f = pd.read_excel("z03_excel.xlsx", sheetname="z02_excel")
print(f)

f1 = pd.ExcelFile("z03_excel.xlsx")
frame = f1.parse("z02_excel", index_col=1)
print(frame)

