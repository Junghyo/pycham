'''
Created on 2017-07-28 16:17

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import pymysql as pms

con = pms.connect(host="localhost",
                  port=3306,
                  user="root",
                  password="1234",
                  db="test",
                  charset="UTF8")
print("connect :", con)
con.close()

