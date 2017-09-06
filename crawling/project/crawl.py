'''
Created on 2017-08-23 14:04

@ product name : PyCharm Community Edition

@ author : yoda
'''


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
from requests.packages import urllib3



ids = []
dates = []
models = []
krnames = []
prices = []
contracts = []
agencies = []
guarantees = []
changes = []
conditions = []
components = []
srcs = []
def mariaDB():
    try:
        con = pms.connect(host="localhost", port=3306, user="root", password="1234", db="test", charset="UTF8")
        cursor = con.cursor()
        for i in range(0, len(ids)):
            cursor.execute("INSERT INTO CETIZEN2 VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            ids[i], dates[i], models[i], krnames[i], prices[i], contracts[i], agencies[i],
            guarantees[i], changes[i], conditions[i], components[i], srcs[i]))
        con.commit()
        print("success")
    except:
        print("error", sys.exc_info())
        con.rollback()
    finally:
        con.close()

def crawl(startno, endno, counter):
    con = pms.connect(host="localhost", port=3306, user="root", password="1234", db="test", charset="UTF8")
    cursor = con.cursor()
    for no in range(startno, endno):
        try:
            url_code = requests.get("http://market.cetizen.com/market.php?q=view&auc_no="+str(no)+"&auc_wireless=5")
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
                            id, date, model, krname, price, contract, agency,
                            guarantee, change, condition, component, src, sold))
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
                pass
            except WindowsError as win:
                pass
            except ConnectionAbortedError as cae:
                pass
            except pms.err.OperationalError as pmsError:
                pass
            except socket.timeout:
                print(str(no)+"timeout")
        except TimeoutError as time:
            print(str(no) + "timeouterror")
            no += 1
            crawl(no, endno, counter)
        except HTTPError as http:
            pass
        except URLError as url:
            pass
        except gaierror as gai:
            pass
        except IOError:
            pass
        except requests.exceptions.ChunkedEncodingError:
            print("#########################" + str(no) + " requests.exceptions.ChuckedEncodingError#########################")
            no += 1
            crawl(no, endno, counter)
        except requests.exceptions.HTTPError:
            print("#########################" + str(no) + " requests.exceptions.HTTPError################################")
            no += 1
            crawl(no, endno, counter)
        except requests.exceptions.ReadTimeout:
            print("#########################" + str(no) + " requests.exceptions.ReadTimeout##########################")
            no += 1
            crawl(no, endno, counter)
        except requests.exceptions.Timeout:
            print("#########################" + str(no) + " requests.exceptions.Timeout#########################")
            no += 1
            crawl(no, endno, counter)
        except urllib3.exceptions.NewConnectionError:
            print("#########################" + str(no) + " urllib3.exceptions.NewConnectionError#########################")
            no += 1
            crawl(no, endno, counter)
        except requests.exceptions.ConnectionError:
            print("#########################" + str(no) + " requests.exceptions.ConnectionError#########################")
            no += 1
            crawl(no, endno, counter)
        except requests.exceptions.RequestException:
            print("#########################" + str(no) + " requests.exceptions.RequestException#########################")
            no += 1
            crawl(no, endno, counter)
        except TypeError:
            print("#########################" + str(no) + " TypeError#########################")
            no += 1
            crawl(no, endno, counter)

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
    pr1 = Process(target=crawl, args=(10231739, 11000000, 1))
    pr2 = Process(target=crawl, args=(11231910, 12000000, 2))
    pr3 = Process(target=crawl, args=(12227555, 13000000, 3))
    pr4 = Process(target=crawl, args=(13259824, 14000000, 4))
    pr5 = Process(target=crawl, args=(14239631, 15000000, 5))
    pr6 = Process(target=crawl, args=(15233491, 16000000, 6))
    pr7 = Process(target=crawl, args=(16236642, 17000000, 7))

    pr1.start()
    pr2.start()
    pr3.start()
    pr4.start()
    pr5.start()
    pr6.start()
    pr7.start()



    pr1.join()
    pr2.join()
    pr3.join()
    pr4.join()
    pr5.join()
    pr6.join()
    pr7.join()


    result.put('STOP')

    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
    log("data crawling completed..")
    log("complete!")
    end_time = time.time()
    print((end_time - start_time)/60)