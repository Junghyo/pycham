'''
Created on 2017-08-18 16:34

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
import pymysql as pms
import sys


# http://music.bugs.co.kr/chart/track/day/total?chartdate=20060922
for y in range(2006, 2018):
    startMonth = 1
    endMonth = 13
    # 벅스뮤직 차트가 2006년 9월부터 시작
    if y == 2006:
        startMonth = 9
    # crawling 당시 날짜 2017년 8월
    elif y == 2017:
        endMonth = 8

    for m in range(startMonth, endMonth):
        startDay = 1
        endDay = 32
        # 벅스뮤직 차트가 2006년 9월 22일부터 시작
        if y == 2006 and m == 9:
            startDay = 22
        # 벅스뮤직 차트가 2017년 8월 17일에 끝
        elif y == 2017 and m == 8:
            endDay = 18

        for d in range(startDay, endDay):
            # 2월달은 28일 또는 29일이 있기도 하기에 28일까지만 수집하기로 고정
            if (m == 2 and d > 28):
                break
            # 4, 6, 9, 11월은 30일까지만 있음
            elif (m in [4, 6, 9, 11] and d > 30):
                break
            # 1~9월은 자리수가 한자리기 때문에 앞에 0을 붙임 ex) 01 ~ 09
            if len(str(m)) < 2:
                mStamp = "0" + str(m)
            else:
                mStamp = str(m)

            # 일도 마찬가지
            if len(str(d)) < 2:
                dStamp = "0" + str(d)
            else:
                dStamp = str(d)

            timeStamp = str(y)+str(mStamp)+str(dStamp)
            # print("날짜: "+timeStamp)

            # timeStamp를 만든 이유는
            # # http://music.bugs.co.kr/chart/track/day/total?chartdate=20060922에서
            # chartdate= 에 값을 넣기 위함

            # url 설정
            url = urlopen("http://music.bugs.co.kr/chart/track/day/total?chartdate="+timeStamp)
            soup = BeautifulSoup(url, "lxml")
            # 가수명 lsit
            artists = []
            artistRank = 0
            # 노래제목 list
            titles = []
            titleRank = 0

            try:
                # <p class="artist">
                for link1 in soup.find_all(name="p", attrs={"class":"artist"}):
                    try:
                        # <p class="artist"> <a>가수명</a> </p>
                        artist = link1.find("a").text
                        artists.append(artist)
                        artistRank += 1
                    # 서비스 되지않는 가수들은 <a> tag가 없음
                    except AttributeError as artistError:
                        artist = "N/A"
                        artists.append(artist)
                        artistRank += 1
                # <p class="title">
                for link2 in soup.find_all(name="p", attrs={"class":"title"}):
                    try:
                        # <p class="title"> <a>노래명</a> </p>
                        title = link2.find("a").text
                        titles.append(title)
                        titleRank += 1
                    # 서비스가 되지않는 노래는 <a> tag가 없음
                    except AttributeError as titleError:
                        title = "N/A"
                        titles.append(title)
                        titleRank += 1

                # artist와 title 목록이 일치하지 않으면 error 발생(디버깅용)
                if(artistRank != titleRank):
                    raise NotImplementedError
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
                    for i in range(0, 100):
                        cursor.execute("INSERT INTO BUGSCHART VALUES(%s, %s, %s, %s)" % (timeStamp, (i+1), str(artists[i]), titles[i]))
                    con.commit()
                except:
                    print("error", sys.exc_info())
                    con.rollback()
                finally:
                    con.close()
            # <p> tag 자체가 없는 경우 데이터가 없다고 여기고 무시하고 지나감
            except AttributeError as e:
                print(timeStamp+": 이 날 데이터는 존재하지 않음")
                continue
            # 위에서 일부러 발생한 error 표시
            except NotImplementedError as notImplemented:
                print(timeStamp+": artist, title 순위 불일치")
            # 웹페이지 자체 에로로 top100이 아니면 index error 표시
            except IndexError as index:
                print(timeStamp+": index Error "+str(len(titles)))








