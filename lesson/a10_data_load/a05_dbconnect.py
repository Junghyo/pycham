'''
Created on 2017-07-28 16:17

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import pymysql as pms
"""
MySQL Client

비밀번호 입력 : 1234

show databases;

use test;

show tables;
char2(50) not null,' at line 3
MariaDB [test]> create table good(
    -> code int primary key,
    -> name varchar(50) not null,
    -> cnt int,
    -> price int);
"""
con = pms.connect(host="localhost",
                  port=3306,
                  user="root",
                  password="1234",
                  db="test",
                  charset="UTF8")
print("connect :", con)
con.close()
