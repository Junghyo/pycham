'''
Created on 2017-07-31 10:50

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

con = pymysql.connect(host='localhost', port=3306, user='root',
                      passwd='1234', db = 'test', charset="utf8")


try:
    cursor = con.cursor()
##  cursor.execute("insert into contact(name, phone) values('홍길동','01078889999') ") ## 삽입
##  cursor.execute("update contact set phone='01088889999' where name='홍길동'") ## 수정
    cursor.execute("delete from contact where name='홍길동' ") ##삭제
    con.commit()
    print("CRUD 성공")
except:
    print("예외발생!!",sys.exc_info())
    con.rollback()
finally:
    con.close()