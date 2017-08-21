'''
Created on 2017-08-21 11:29

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
from bs4 import BeautifulSoup
from urllib.request import urlopen

f=open('cetizen.txt','w', encoding='utf-8')
f.write("모델명,가격,날짜,as무상보증기간,약정여부,기기변경여부,상태\n")



for p in range(2, 3):
    page = str(p)
    url = urlopen("http://market.cetizen.com/market.php?auc_sale=1&auc_wireless=5&p="+page)
    soup = BeautifulSoup(url, "lxml")
    models = []
    prices = []
    dates = []
    guarantees = []
    contracts = []
    changes = []
    conditions = []

    try:
        # model명
        for link1 in soup.find_all(name="div", attrs={"style":"overflow:hidden;cursor:hand;cursor:pointer;margin-top:2px;margin-left:5px;"}):
            try:
                model = link1.find("span").text
                print(model)
                models.append(model)
            # 해당 tag가 없을 경우 "N/A"로 데이터값 삽입
            except AttributeError as modelError:
                model = "N/A"
                models.append(model)
        # price
        for link2 in soup.find_all(name="li", attrs={"style":"width:8%;float:left;overflow:hidden;text-align:right;"}):
            try:
                price = link2.find("span").text
                price = str.replace(price, ",", "")
                prices.append(price)
            # 해당 tag가 없을 경우 "N/A"로 데이터값 삽입
            except AttributeError as priceError:
                price = "N/A"
                prices.append(price)
        # date
        for link3 in soup.find_all(name="li", attrs={"style":"width:5%;float:left;overflow:hidden;text-align:center;padding-top:2px;"}):
            try:
                date = link3.find("span").text
                # 만약 date에 ":" or "전"이 포함되어 있으면 오늘 날짜로(crawling 당시 날짜 : 2017-08-21)
                if ":" or "전" in date:
                    dates.append("2017-08-21")
                else:
                    dates.append(date)
            # 해당 tag가 없을 경우 "N/A"로 데이터값 삽입
            except AttributeError as dateError:
                date = "N/A"
                dates.append(date)
        # option
        for link4 in soup.find_all(name="li", attrs={"style":"width:16%;float:right;overflow:hidden;padding-right:0px;text-align:right;"}):
            # 옵션값이 빈칸이 아닐 경우
            if link4.findChildren()[0].text != "" :
                try:
                    # guarantee = 보증 / A/S / 만료
                    guarantee = link4.findChildren()[0].text
                    guarantees.append(guarantee)
                    # contract = 선택약정 / 불가 / 모름
                    contract = link4.findChildren()[1].text
                    contracts.append(contract)
                    # changes = 유심기변 / 확정기변 / 모름
                    change = link4.findChildren()[2].text
                    changes.append(change)
                    # conditions = 물건 상태(미사용 / 상/ 중 / 하)
                    condition = link4.findChildren()[3].text
                    conditions.append(condition)
                # 해당 tag가 없을 경우 "N/A"로 데이터값 삽입
                except AttributeError as optionError:
                    guarantee = "N/A"
                    contract = "N/A"
                    change = "N/A"
                    condition = "N/A"
                    guarantees.append(guarantee)
                    contracts.append(contract)
                    changes.append(change)
                    conditions.append(condition)
            # 옵션값이 빈칸일 경우
            else:
                try:
                    guarantee = "N/A"
                    contract = "N/A"
                    change = "N/A"
                    condition = "N/A"
                    guarantees.append(guarantee)
                    contracts.append(contract)
                    changes.append(change)
                    conditions.append(condition)
                except:
                    pass

        for i in range(0, 20):
            f.write(str(models[i]) + "," +
                    str(prices[i]) + "," +
                    str(dates[i]) + "," +
                    str(guarantees[i]) + "," +
                    str(contracts[i]) + "," +
                    str(changes[i]) + "," +
                    str(conditions[i]) + '\n')
    # 각 필요한 데이터들이 없는 경우 데이터가 없다고 여기고 무시하고 지나감
    except AttributeError as e:
        print("이날 데이터 없음")
        continue
    # 각 페이지마다 총 20개가 있는데 웹페이지 자체 에러로 index가 모자른 경우 error 표시
    except IndexError as index:
        print("out of index 해당 페이지 : " + page)

f.close()
print(models)








