'''
Created on 2017-08-01 10:56

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import pymysql as pms
import sys

con = pms.connect(host="localhost",
                  port=3306,
                  user="root",
                  passwd="1234",
                  db="test",
                  charset="utf8")
try:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM STOCK")
    f = cursor.fetchall()
except:
    print("error :", sys.exc_info())
finally:
    con.close()

l = list(f)
df = pd.DataFrame(l, columns=["num", "date", "name", "price", "count"])
print(df)

div()
print(df.pivot("date", "name"))

div()
# num 컬럼 삭제
df1 = df.drop("num", axis=1)
print(df1.pivot("date", "name"))