'''
Created on 2017-07-31 10:36

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import pymysql as pms
import sys
"""
 python에서 data 검색
 1. 연결객체의 cursor() 호출, sql실행 객체를 가져옮
 
 2. execute(query문)
 
 3. cursor 객체를 가지고 fetchone()/fetchall()를 호출하면 tuple형태로 결과가 return
 
 4. list로 전환
    1) list = []
    2) append() 활용
        for i in data:
        lost.append(i)
 
 5. DataFrame으로 전환
    3) list를 첫번째 parameter로
    4) columns = [컬럼명1, 컬럼명2, 컬럼명3]
 
"""
con = pms.connect(
    host="35.190.226.198",
    port=3306,
    user="CTO",
    passwd="abc123",
    db="test",
    charset="utf8"
)

try:
    cursor = con.cursor()
    # cursor.execute("INSERT INTO DEPT VALUES('40', '발령대기', '경기 성남') ")
    # con.commit()
    cursor.execute("SELECT id, date FROM totalzen")
    # 첫번째 행만
    # data = cursor.fetchone()
    # print(data)
    # for i in data:
    #     print(i)
    48
    # 모든 데이터
    l1 = []
    data = cursor.fetchall()
    c_id = 10000037
    for i in data:
        if (i[0] - c_id > 2000):
            c_id = i[0]
            print(i[1])
            cursor.execute("SELECT max(id), min(id) FROM totalzen WHERE date = '%s'" % i[1])
            data = cursor.fetchall()
            for y in data:
                print(y)

            # print(i[1]
except:
    print("excpetion", sys.exc_info())

finally:
    con.close()




div()

