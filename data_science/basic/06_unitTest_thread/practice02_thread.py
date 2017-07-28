'''
Created on 2017-07-24 18:49

@ product name : PyCharm Community Edition

@ author : yoda
'''


"""
 # thread
 
 python program은 기본적으로 single thread에서 실행.
 코드를 병렬로 실행하기 위해서는 subthread를 생성해야하는데 
 이 때 사용하는 것이 threading module 이다.
 
 
 # threading module
 
 threading 모듈의 threading.Thread() 함수를 호출하여 Thread 객체를 얻은 후
 thread 객체의 start() 메서드를 호출하면 된다.
"""

"""
 (1) 쓰레드가 실행할 함수 혹은 메서드를 작성
 
 쓰레드가 실행할 함수 (혹은 메서드)를 작성하고
 그 함수명을 hreading.Thread() 함수의 target 아큐먼트에 지정하면 된다.
"""

import threading
import time
def plus(a, b):
    total = 0
    for i in range(a, b):
        total += i
        print("sub thread :", i)
        time.sleep(0.001)
    print("sub thread :", total)

t = threading.Thread(target=plus, args=(1, 100000))
t.start()

for i in range(1, 100):
    print("main thread :"+str(i))
    time.sleep(0.1)

# 동시에 시작된다.



"""
 (2) threading.Thread 로부터 파생된 파생클래스를 작성하여 사용하는 방식
 
 Thread 클래스를 파생하여 쓰레드가 실행할 run() 메서드를 재정의해서 사용하는 방식이다.
 Thread 클래스에서 run() 메서드는 쓰레드가 실제 실행하는 메서드이며, 
 start() 메서드는 내부적으로 이 run() 메서드를 호출한다
"""

import threading, requests, time


def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')


t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.start()



import threading, requests, time


class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), ' chars')


t = HtmlGetter('http://google.com')
t.daemon = True # demon thread : main thread가 종료되면 수행하지 않고 종료하게 된다.
t.start()

print("### End ###")
