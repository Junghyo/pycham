'''
Created on 2017-08-25 10:52

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns
import scipy as sp
import scipy.stats as stats
import pymysql as pms
import sys
con = pms.connect(
    host="192.168.0.18",
    port=3306,
    user="root",
    passwd="1234",
    db="test",
    charset="utf8"
)

try:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM CETIZEN WHERE ID = 16223419")
    li = []
    data = cursor.fetchone()
    for i in data:
        li.append(i)
except:
    print(sys.exc_info())
finally:
    con.close()

l = list(data)
print(l)