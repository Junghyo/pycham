'''
Created on 2017-08-23 14:04

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
from urllib.error import *
from socket import *
import requests
from requests.adapters import HTTPAdapter
from requests.packages import urllib3
from requests.packages.urllib3.util.retry import Retry
import threading


class crawlThread(threading.Thread):
    def __init__(self, startno, endno, counter):
        super(crawlThread, self).__init__()
        self.startno = startno
        self.endno = endno
        self.thread_no = counter
    def run(self):
        print("Starting"+self.getName())
        self.crawl()
    def crawl(self):
        con = pms.connect(host="localhost", port=3306, user="root", password="1234", db="test", charset="UTF8")
        cursor = con.cursor()
        try:
            for no in range(self.startno, self.endno):
                s = requests.Session()
                retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
                s.mount('http://', HTTPAdapter(max_retries=retries))
                url_code = s.get("http://market.cetizen.com/market.php?q=view&auc_no="+str(no)+"&auc_wireless=5", timeout=2)
                plain_text = url_code.text
                soup = BeautifulSoup(plain_text, "lxml")
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
                    try:
                        krname = soup.find(name="li", attrs={"class":"viewright_box_wide p17 clr100 b"}).text
                        krname = str.split(krname, "\xa0")[0]
                        krname = str.replace(krname, "\xa0", "")
                    except AttributeError as krnamesError:
                        krname = "N/A"
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
                    try:
                        src = soup.find(name="img", attrs={"width":"220", "vspace":"1"}).get("src")
                    except AttributeError as srcsError:
                        src = "N/A"
                    try:
                        sold = soup.find(name="span", attrs={"class":"p13 clr100 b"}).text
                    except AttributeError as soldError:
                        sold = "N/A"
                    print(str(no)+" crawling completed")
                    try:
                        cursor.execute("INSERT INTO CETIZEN VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                                id, date, model, krname, price, contract, agency, guarantee,
                                change, condition, component, src, sold))
                        con.commit()
                    except:
                        print("error", sys.exc_info())
                        con.rollback()
                    print(str(no)+" inserting sql completed")
                except AttributeError as e:
                    print(str(no) + "데이터 존재하지 않음")
                    continue
                except IndexError as index:
                    print(str(no)+"IndexError")
                except URLError as e:
                    print(str(no)+"URLError")
                except HTTPError as http:
                    pass
                except WindowsError as win:
                    pass
                # except socket.timeout:
                #     print(str(no)+" timeout")
        except gaierror as gai:
            print("#############################process" + str(counter) + " : " + str(no) + "gaierror##############################")
            no += 1
            crawl(no, endno, counter)
        except TimeoutError as time:
            print("#############################process" + str(counter)+" : " + str(no) + "TimeoutError##############################")
            no += 1
            crawl(no, endno, counter)
        except requests.packages.urllib3.exceptions.ProtocolError:
            print("##############################process" + str(counter)+" : " + str(no) + " requests.packages.urllib3.exceptions.ProtocolError##############################")
            no += 1
        except requests.exceptions.ChunkedEncodingError:
            print("##############################process" + str(counter)+" : " + str(no) + " requests.exceptions.ChunkedEncodingError##############################")
            no += 1
            crawl(no, endno, counter)
        except ConnectionRefusedError:
            print("##############################process" + str(counter) + " : " + str(no) + " ConnectionRefusedError##############################")
            no += 1
            crawl(no, endno, counter)
        except urllib3.exceptions.NewConnectionError:
            print("##############################process" + str(counter) + " : " + str(no) + " urllib3.exceptions.NewConnectionError##############################")
            no += 1
            crawl(no, endno, counter)
        except urllib3.exceptions.MaxRetryError:
            print("##############################process" + str(counter) + " : " + str(no) + " urllib3.exceptions.MaxRetryError##############################")
            no += 1
            crawl(no, endno, counter)
        except requests.exceptions.ConnectionError:
            print("##############################process" + str(counter) + " : " + str(no) + " requests.exceptions.ConnectionError##############################")
            no += 1
            crawl(no, endno, counter)
        except requests.exceptions.RequestException:
            print("##############################process" + str(counter) + " : " + str(no) + " requests.exceptions.RequestException##############################")
            no += 1
            crawl(no, endno, counter)
        log("saving that to mysql..")
        print("process" + str(counter) + " success")
        end_time = time.time()
        print((end_time - start_time) / 60)





def log(message):
	ts = time.time()
	sts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print ("%s : %s"% (sts, message))

log("start crawl..")

start_time = time.time()
t1 = crawlThread(1, 10000, 1)
t2 = crawlThread(10000, 20000, 2)
t3 = crawlThread(20000, 30000, 3)
t4 = crawlThread(30000, 40000, 4)
t1.start()
t2.start()
t3.start()
t4.start()
