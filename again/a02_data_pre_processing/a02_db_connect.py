'''
Created on 2017-08-07 19:59

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
import cx_Oracle as co
# MariaDB에 Python으로 접속하여 SQL query 해서 pandas DataFrame 만들기

def maria(query):
    import pymysql as pms
    from datetime import datetime
    # DB connect
    conn = pms.connect(host="localhost",
                       port=3306,
                       user="root",
                       passwd="1234",
                       db="test")
    # start time
    start = datetime.now()

    # get a dataframe
    global query_result
    query_result = pd.read_sql(query, conn)

    # close connection
    end = datetime.now()

    print("start :", str(start))
    print("end :", str(end))
    print("elap time :", str(end-start))
    conn.close()

    return query_result

query = "SELECT * FROM DEPT"

maria(query)
print(query_result)