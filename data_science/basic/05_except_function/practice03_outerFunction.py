'''
Created on 2017-07-24 14:20

@ product name : PyCharm Community Edition

@ author : yoda
'''


"""
 python library
 
"""

"""
 sys
 
 sys 모듈은 파이썬 인터프리터가 제공하는 변수들과 함수들을
 직접 제어할 수 있게 해주는 모듈이다.
"""
print("=" * 50)
print("1. sys")
print("=" * 50)

import sys

# 1. 명령 행에서 인수 전달하기 - sys.argv
print(sys.argv)

# 2. 강제로 스크립트 종료하기 - sys.exit
# sys.exit()

# 3. 자신이 만든 모듈 불러와 사용하기 - sys.path
sys.path.append("C:/pycharm/basic/myModules") # 자신의 module package 등록
print(sys.path)


"""
 pickle
 
 pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
 다음 예는 pickle 모듈의 dump 함수를 이용하여 딕셔너리 객체인 data를
 그대로 파일에 저장하는 방법을 보여 준다.
"""
print("=" * 50)
print("2. pickle")
print("=" * 50)

import pickle
f = open("test.txt", "wb")
data = {1: 'python', 2: "you need"}
pickle.dump(data, f)
f.close()

f1 = open("test.txt", "rb")
data = pickle.load(f1)
print(data) # {1: 'python', 2: 'you need'}


"""
 os
 
 OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.
"""
print("=" * 50)
print("2. os")
print("=" * 50)

import os

# 내 시스템의 환경 변수값을 알고 싶을 때 - os.environ
print(os.environ)
print(os.environ['PATH'])

# 디렉터리 위치 변경하기 - os.chdir
# os.chdir("C:\WINDOWS")

# 디렉터리 위치 리턴받기 - os.getcwd
print(os.getcwd())

# 시스템 명령어 호출하기 - os.system
print(os.system("dir"))

# 실행한 시스템 명령어의 결과값 return받기 - os.popen
f = os.popen("dir")
print(f.read())

"""
 기타 유용한 os 관련 함수
 
 함수	                                설명
 os.mkdir(디렉터리)	            디렉터리를 생성한다.
 os.rmdir(디렉터리)	            디렉터리를 삭제한다.단, 디렉터리가 비어있어야 삭제가 가능하다.
 os.unlink(파일)	                파일을 지운다.
 os.rename(src, dst)	        src라는 이름의 파일을 dst라는 이름으로 바꾼다.
"""

"""
 shutil
 
 파일을 복사해 주는 파이썬 모듈이다.
"""
print("=" * 50)
print("3. shutil")
print("=" * 50)

# 파일 복사하기 - shutil.copy(src, dst)
import shutil

shutil.copy("test.txt", "copy.txt")


"""
 glob
 
 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면
 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다.
 이럴 때 사용하는 모듈이 바로 glob이다.
"""
print("=" * 50)
print("4. glob")
print("=" * 50)

# 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)

import glob

g_list = glob.glob("C:\\pycharm\\basic\\05_except_function\\*")
print(g_list)


"""
 tempfile
 
 파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다.
 tempfile.mktemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 리턴한다.
 
 tempfile.TemporaryFile()은 임시 저장 공간으로 사용될 파일 객체를 리턴한다.
 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다.
 f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.
"""
print("=" * 50)
print("5. tempfile")
print("=" * 50)

import tempfile

fname = tempfile.mkdtemp()
print(fname)

f = tempfile.TemporaryFile()
print(f.read())
f.close()

"""
 time
"""
print("=" * 50)
print("6. time")
print("=" * 50)

# time.time : 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴한다.

import time

print(time.time())  # 1500882734.5148146

# time.localtime : time.time()에 의해서 반환된 실수값을 이용해서
#                  연도, 월, 일, 시, 분, 초,.. 의 형태로 바꾸어 주는 함수이다.

print(time.localtime())
# time.struct_time(tm_year=2017, tm_mon=7, tm_mday=24, tm_hour=16, tm_min=53,
#                   tm_sec=51, tm_wday=0, tm_yday=205, tm_isdst=0)

# time.asctime() : 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수이다.
print(time.asctime())   # Mon Jul 24 16:56:56 2017

# time.ctime() : asctime과 다른점은 ctime은 항상 현재 시간만을 return
print(time.ctime())

time_ex = time.ctime().split(sep=" ")
for i in time_ex:
    print(i)


"""
 time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
 
 포맷코드	        설명	                                예
 %a	                요일 줄임말	                        Mon
 %A	                요일	                                Monday
 %b	                달 줄임말	                        Jan
 %B	                달	                                January
 %c	                날짜와 시간을 출력함	                06/01/01 17:22:21
 %d	                날(day)	                            [00,31]
 %H	                시간(hour)-24시간 출력 형태	        [00,23]
 %I	                시간(hour)-12시간 출력 형태	        [01,12]
 %j	                1년 중 누적 날짜	                    [001,366]
 %m	                달	                                [01,12]
 %M	                분	                                [01,59]
 %p	                AM or PM	                        AM
 %S	                초	                                [00,61]
 %U	                1년 중 누적 주-일요일을 시작으로	    [00,53]
 %w	                숫자로 된 요일	                    [0(일요일),6]
 %W	                1년 중 누적 주-월요일을 시작으로	    [00,53]
 %x	                현재 설정된 로케일에 기반한 날짜 출력	06/01/01
 %X	                현재 설정된 로케일에 기반한 시간 출력	17:22:21
 %Y	                년도 출력	                        2001
 %Z	                시간대 출력	                        대한민국 표준시
 %%	                문자                              	%
 %y	                세기부분을 제외한 년도 출력	        01
 
"""

print(time.strftime("%Y %x %p %I:%M:%S"))   # 2017 07/24/17 PM 05:06:21

# time.sleep : 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다.

for i in range(10):
    print(i)
    # time.sleep(1)   # 1초 간격으로 출력


"""
 calendar
"""
print("=" * 50)
print("7. calendar")
print("=" * 50)

# calendar.calendar(year) : 그 해의 전체 달력 보기
import calendar

print(calendar.calendar(2015))
calendar.prcal(2017) # print 안해도 출력

calendar.prmonth(2017, 7) # 해당년도 해당월만 보여줌

# calendar.weekday : 해당 날짜의 요일값을 return
print( calendar.weekday(2017, 7, 24) )  # 0
# 월요일은 0, 화요일은 1, 수요일은 2, 목요일은 3, 금요일은 4, 토요일은 5, 일요일은 6

# calendar.monthrange : 해당년도, 월의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지 tuple로 return
print( calendar.monthrange(2017, 7) )   # (5, 31) 토요일, 31일까지 있음

"""
 random
 
 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다. random과 randint에 대해서 알아보자.
"""
print("=" * 50)
print("8. random")
print("=" * 50)

# 0.0 ~ 1.0 사이의 난수값 return
import random

print( random.random() )

# 1 ~ 10 사이의 정수 중에서 난수값 return
print( random.randint(1, 10) )

def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

data = [1, 2, 3, 4, 5]

while data:
    print(random_pop(data))
    print(data)

print(data) # data가 없어짐 []

def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number

data2 = ["a", "b", "c", "d", "e"]

while data2:
    print(data2)
    print(random_pop2(data2))


# list 항목을 무작위로 섞고 싶을 때는? shuffle 사용
data3 = list( range(1, 21) )
print(data3)
random.shuffle(data3)
print(data3)


"""
 webbrowser
 
 webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저가 자동으로 실행되게 하는 모듈이다.
"""
print("=" * 50)
print("9, webbrowser")
print("=" * 50)

import webbrowser

# 아래의 예제는 웹 브라우저를 자동으로 실행시키고 해당 URL인 http://google.com으로 가게 해준다.
# webbrowser.open("http://google.com")


"""
 threading
 
 컴퓨터에서 동작하고 있는 프로그램을 프로세스(Process)라고 한다.
 보통 1개의 프로세스는 1가지 일만 하지만, 
 스레드를 이용하면 한 프로세스 내에서 2가지 또는 그 이상의 일을 동시에 수행하게 할 수 있다.
"""

import threading

def say(msg):
    while True:
        time.sleep(1)
        print(msg)


for msg in ["process"+str(i) for i in range(1, 6)]:
    t = threading.Thread(target=say, args=(msg, ))
    t.daemon = True
    t.start()

for i in  range(100):
    time.sleep(0.1)
    print(i)

# 첫 번째 for문에서 ['you', 'need', 'python']이라는 리스트의 요소 개수만큼 스레드가 생성되고,
# 생성된 스레드는 say 메서드를 수행하게 되어 1초에 한 번씩 입력으로 받은 msg 변수값을 리턴한다.
# 두 번째 for문은 매 0.1초마다 0부터 99까지 숫자를 출력하는데, 바로 이 부분이 메인 프로그램이 되며
# 이 메인 프로그램이 종료되는 순간 생성된 스레드들도 함께 종료가 된다.
# t.daemon = True와 같이 daemon 플래그를 설정하면 주 프로그램이 종료되는 순간 데몬 스레드도 함께 종료된다.

# threading.Thread class

class MyThread(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg = msg
        self.daemon = True

    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)


for msg in ["thread1", "thread2"]:
    t = MyThread(msg)
    t.start()


for i in range(100):
    time.sleep(0.1)
    print(i)

# 스레드를 클래스로 정의할 경우에는 __init__ 메서드에서
# threading.Thread.__init__(self)와 같이 부모 클래스의 생성자를 반드시 호출해야 한다.
# MyThread로 생성된 객체의 start 메서드를 실행할 때는 MyThread 클래스의 run 메서드가 자동으로 수행된다.