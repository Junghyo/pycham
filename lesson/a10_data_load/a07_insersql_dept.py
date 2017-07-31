'''
Created on 2017-07-31 10:39

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import pymysql as pms
import sys

try:
    con = pms.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        db="test",
        charset="UTF8"
    )
    cursor = con.cursor()
    cursor.execute("INSERT INTO DEPT VALUES(10, '인사과', '서울 강남')")
    cursor.execute("INSERT INTO DEPT VALUES(20, '총무', '서울 강북')")
    cursor.execute("INSERT INTO DEPT VALUES(30, 'IT사업부', '서울 송파')")
    con.commit()
    print("success")
except:
    print("error", sys.exc_info())
    con.rollback()
finally:
    con.close()
