'''
Created on 2017-08-21 15:13

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

class crawlThread(threading.Thread):
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
    def __init__(self, startno, endno, counter):
        super(crawlThread, self).__init__()
        self.startno = startno
        self.endno = endno
        self.thread_no = counter

    def run(self):
        print("Starting"+self.getName())
        self.crawl()

    def crawl(self):
        for no in range(self.startno, self.endno):
            url = urlopen("http://market.cetizen.com/market.php?q=view&auc_no="+str(no))
            soup = BeautifulSoup(url, "lxml")
            # ids
            id = no
            # dates
            try:
                try:
                    date = soup.find(name="span", attrs={"class":"p12 ls-0"}).text
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
                self.ids.append(id)
                self.dates.append(date)
                self.models.append(model)
                self.prices.append(price)
                self.contracts.append(contract)
                self.agencies.append(agency)
                self.guarantees.append(guarantee)
                self.changes.append(change)
                self.conditions.append(condition)
                self.components.append(component)
            except AttributeError as e:
                print(str(no) + "데이터 존재하지 않음")
                continue
            except IndexError as index:
                print(str(no)+"IndexError")
        print(self.ids)
        print(len(self.ids))
        print(self.dates)
        print(self.models)
        print(self.prices)
        print(self.contracts)
        print(len(self.contracts))
        print(self.agencies)
        print(len(self.agencies))
        print(self.guarantees)
        print(len(self.guarantees))
        print(self.changes)
        print(len(self.changes))
        print(self.conditions)
        print(len(self.conditions))
        print(self.components)
        print(len(self.components))
    def getdata(self):
        return self.ids, self.dates, self.models



t1 = crawlThread(17391094, 17391114, 1)
t1.start()



