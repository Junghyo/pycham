'''
Created on 2017-08-23 11:37

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

tablets_before = []
tablets_after = []
wearables_before = []
wearables_after = []
generals_before = []
generals_after = []


# tablet model crawling
def crawl_t(startPage, endPage, counter):
    for page in range(startPage, endPage):
        url = urlopen("http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&view_type=&just_one=&just_one_pcat=&just_one_name=&cat%5B1%5D=2&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&escrow_motion=3&p="+str(page))
        soup = BeautifulSoup(url, "lxml")
        try:
            for link1 in soup.find_all(name="div", attrs={"style": "overflow:hidden;cursor:hand;cursor:pointer;margin-top:2px;margin-left:5px;"}):
                tablet = link1.find("span").text
                tablets_before.append(tablet)
            print("tablet "+str(page)+"page crawling completed")
        except AttributeError as tabletError:
            tablet = ""
            tablets_before.append(tablet)
    tablets_after = list(set(tablets_before))
    try:
        con = pms.connect(host="localhost", port=3306, user="root", password="1234", db="test", charset="UTF8")
        cursor = con.cursor()
        for i in range(0, len(tablets_after)):
            cursor.execute("INSERT INTO TABLETS VALUES('%s')" % (tablets_after[i]))
        con.commit()
        print("success")
    except:
        print("error", sys.exc_info())
        con.rollback()
    finally:
        con.close()
    print("tablets finished")


# wearable model crawling
def crawl_w(startPage, endPage, counter):
    for page in range(startPage, endPage):
        url = urlopen("http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&cat%5B3%5D=10&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p="+str(page))
        soup = BeautifulSoup(url, "lxml")
        try:
            for link1 in soup.find_all(name="div", attrs={"style": "overflow:hidden;cursor:hand;cursor:pointer;margin-top:2px;margin-left:5px;"}):
                wearable = link1.find("span").text
                wearables_before.append(wearable)
            print("wearable "+str(page)+"page crawling completed")
        except AttributeError as wearableError:
            wearable = ""
            wearables_before.append(wearable)
    wearables_after = list(set(wearables_before))
    try:
        con = pms.connect(host="localhost", port=3306, user="root", password="1234", db="test", charset="UTF8")
        cursor = con.cursor()
        for i in range(0, len(wearables_after)):
            cursor.execute("INSERT INTO WEARABLES VALUES('%s')" % (wearables_after[i]))
        con.commit()
        print("success")
    except:
        print("error", sys.exc_info())
        con.rollback()
    finally:
        con.close()
    print("wearables finished")


# general phone model crawling
def crawl_g(startPage, endPage, counter):
    for page in range(startPage, endPage):
        url = urlopen("http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&cat%5B2%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p="+str(page))
        soup = BeautifulSoup(url, "lxml")
        try:
            for link1 in soup.find_all(name="div", attrs={"style": "overflow:hidden;cursor:hand;cursor:pointer;margin-top:2px;margin-left:5px;"}):
                general = link1.find("span").text
                generals_before.append(general)
            print("general "+str(page)+"page crawling completed")
        except AttributeError as generalError:
            general = ""
            generals_before.append(general)
    generals_after = list(set(generals_before))
    try:
        con = pms.connect(host="localhost", port=3306, user="root", password="1234", db="test", charset="UTF8")
        cursor = con.cursor()
        for i in range(0, len(generals_after)):
            cursor.execute("INSERT INTO GENERALS VALUES('%s')" % (generals_after[i]))
        con.commit()
        print("success")
    except:
        print("error", sys.exc_info())
        con.rollback()
    finally:
        con.close()
    print("generals finished")

def log(message):
	ts = time.time()
	sts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print ("%s : %s"% (sts, message))

log("start crawl..")

if __name__ == '__main__':
    start_time = time.time()
    result = Queue()
    pr1 = Process(target=crawl_t, args=(1, 19, 1))
    pr2 = Process(target=crawl_w, args=(1, 5, 2))
    pr3 = Process(target=crawl_g, args=(1, 65, 3))

    pr1.start()
    pr2.start()
    pr3.start()

    pr1.join()
    pr2.join()
    pr3.join()

    result.put('STOP')

    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break

    log("complete!")

    end_time = time.time()
    print((end_time - start_time)/60)