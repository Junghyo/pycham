'''
Created on 2017-07-31 10:07

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import pymysql as pms
import sys

"""
파이썬에서 삽입과 삭제 또는 갱신..
1. 연결객체인 pymysql.connect()에 있는 cursor() 메서드를 호출하여..
    sql(insert into 테이블명 values(##,##,##)) 명령으로 처리한다.
2. excute( sql 명령어 )
3. 연결 객체에 있는 commit() 호출로 반영, rollback() 호출하여 취소
   처리된다.
4. 예외 처리..
    try:
        연결및 sql 처리, commit()
    except:
        예외발생시 처리할 내용, rollback()
    finally:
        정상 처리 및 예외 발생 여부 상관 없이 처리
        con.close()
"""


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
    cursor.execute("INSERT INTO CONTACT VALUES('홍길동', '01078889999')")
    con.commit()
    print("success")
except:
    print("error", sys.exc_info())
    con.rollback()
finally:
    con.close()