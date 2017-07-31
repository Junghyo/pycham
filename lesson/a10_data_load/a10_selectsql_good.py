'''
Created on 2017-07-31 11:15

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import pymysql as pms
import sys

con = pms.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="1234",
    db="test",
    charset="utf8"
)

try:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM GOOD")
    data = cursor.fetchall()
    print("success")
except:
    print("error", sys.exc_info() )
finally:
    con.close()

l = list(data)
df = pd.DataFrame(l, columns=["code", "name", "count", "price"])
print(df)