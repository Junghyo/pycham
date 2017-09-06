'''
Created on 2017-08-22 12:02

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
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading
import sys
import re
import datetime, time
from multiprocessing import Process, Queue
import pymysql as pms

ids = []
dates = []
models = []
prices = []
contracts = []
agencies = []
guarantees = []
changes = []
conditions = []
components = []
def mariaDB():
    try:
        con = pms.connect(host="localhost", port=3306, user="root", password="1234", db="test", charset="UTF8")
        cursor = con.cursor()
        for i in range(0, len(ids)):
            cursor.execute("INSERT INTO CETIZEN VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            ids[i], dates[i], models[i], prices[i], contracts[i], agencies[i],
            guarantees[i], changes[i], conditions[i], components[i]))
        con.commit()
        print("success")
    except:
        print("error", sys.exc_info())
        con.rollback()
    finally:
        con.close()

def crawl(startno, endno, counter):
    for no in range(startno, endno):
        url = urlopen("http://market.cetizen.com/market.php?q=view&auc_no="+str(no)+"&auc_wireless=5")
        soup = BeautifulSoup(url, "lxml")
        # ids
        id = no
        # dates
        try:
            try:
                date = soup.find(name="span", attrs={"class":"p12 ls-0"}).text
                date = date[1:11]
            except AttributeError as datesError:
                date = "N/A"
            # models
            try:
                model = soup.find(name="span", attrs={"class":"clr02 bn p15 ls-0"}).text
            except AttributeError as modelsError:
                model = "N/A"
            # prices
            try:
                price = soup.find(name="span", attrs={"class":"clr03 p21"}).text
                price = re.sub('[^0-9]', "", price)
            except AttributeError as pricesError:
                price = "N/A"
            # contracts
            try:
                contract = soup.find(name="span", attrs={"onmouseout":"OnIconHide('opt"+str(no)+"');"}).text
            except AttributeError as contractsError:
                contract = "N/A"
            # agencies
            try:
                agency = soup.find(name="li", attrs={"class":"viewright_box_wide clr04"}).text
                agency = str.replace(agency, "\xa0", "")
            except AttributeError as agenciesError:
                agency = "N/A"
            # guarantees
            try:
                guarantee = soup.find(name="li", attrs={"class":"viewright_box clr04 "}).text
            except AttributeError as guaranteesError:
                guarantee = "N/A"
            # changes
            try:
                change = soup.find(name="span", attrs={"onmouseout":"OnIconHide('usim"+str(no)+"');"}).text
            except AttributeError as changesError:
                change = "N/A"
            # conditions
            try:
                condition = soup.find_all(name="li", attrs={"class":"viewright_box clr04 "})[1].text
            except AttributeError as conditionsError:
                condition = "N/A"
            # components
            try:
                component = soup.find_all(name="li", attrs={"class":"viewright_box1 clr04"})[1].text
            except AttributeError as componentError:
                component = "N/A"
            ids.append(id)
            dates.append(date)
            models.append(model)
            prices.append(price)
            contracts.append(contract)
            agencies.append(agency)
            guarantees.append(guarantee)
            changes.append(change)
            conditions.append(condition)
            components.append(component)
            print(str(no)+" crawling completed")
        except AttributeError as e:
            print(str(no) + "데이터 존재하지 않음")
            continue
        except IndexError as index:
            print(str(no)+"IndexError")
    log("saving that to mysql..")
    mariaDB()
    print("process" + str(counter) + " success")





def log(message):
	ts = time.time()
	sts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print ("%s : %s"% (sts, message))

log("start crawl..")

if __name__ == '__main__':
    start_time = time.time()
    result = Queue()
    pr1 = Process(target=crawl, args=(17419037, 17419237, 1))
    pr2 = Process(target=crawl, args=(17419237, 17419437, 2))
    pr3 = Process(target=crawl, args=(17419437, 17419637, 3))
    pr4 = Process(target=crawl, args=(17419637, 17419837, 4))
    pr5 = Process(target=crawl, args=(17419837, 17420037, 5))
    # 17420881

    pr1.start()
    pr2.start()
    pr3.start()
    pr4.start()
    pr5.start()


    pr1.join()
    pr2.join()
    pr3.join()
    pr4.join()
    pr5.join()


    result.put('STOP')

    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
    log("data crawling completed..")
    log("complete!")
    end_time = time.time()
    print((end_time - start_time)/60)
