'''
Created on 2017-07-24 10:06

@ product name : PyCharm Community Edition

@ author : yoda
'''
from abc import abstractclassmethod

"""
 try ~ except
 
 try 블록 실행 중에 오류가 발생하면 except 블록 수행
 
 1. try ~ except
 try:
    ...
except:
    ...

 2. 발생 오류만 포함한 except문
 try:
    ...
except 발생 오류:
    ...

 3. 발생 오류와 오류 메시지 변수까지 포함한 except문
 try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...
"""

# 4/0   ZeroDivisionError: division by zero

try:
    4/0
except ZeroDivisionError as e:
    print(e)    # division by zero


"""
 4. try ~ else
 
 오류가 발생하면  except절 실행
 발생하지 않는다면 else절 실행
"""
try:
    f = open("none.file", "r")
except FileNotFoundError as e:
    print(str(e))   # [Errno 2] No such file or directory: 'none.file'
else:
    data = f.read()
    f.close()

"""
 5. try ~ finally
 try 구문에서 예외발생 상관없이 finally 절 수행
"""
f = open("foo.txt", "w")
try:
    data = "Hello, try~finally"
    f.write(data)
finally:
    f.close()
# try 문이 수행된 후 예외 발생 여부 상관없이 finally 절에서 f.close() 수행

"""
 6 .여러개의 오류처리하기
 try:
    ...
except 발생 오류1:
   ... 
except 발생 오류2:
   ...
"""
try:
    a = [1, 2, 3]
    print(a[3])
    4 / 0
except ZeroDivisionError as e1:
    print(str(e1)+": 0으로 나눌수 없습니다.")
except IndexError as e2:
    print(str(e2)+": indexing을 할 수 없습니다.")
# print(a[3])을 먼저 수행하여 indexError가 먼저 발생하기에 4/0으로 발생하는
# ZeroDivisionError는 발생하지 않는다.

try:
    a= [1, 2, 3]
    4 / 0
    print(a[3])
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 다음과 같이 한번에 묶어서 처리할 수 있다.(이 때도 첫번째 error가 발생하면 이후에는 수행되지 않는다.)

"""
 7. except 회피하기
 
 pass를 이용
"""
try:
    f = open("none.file", "r")
except FileNotFoundError:
    pass

"""
 8. except 일부러 발생시키기
 
 raise라는 명령어를 이용해 강제로 오류 발생
"""
class Bird:
    def fly(self):
        raise NotImplementedError

# class Eagle(Bird):
#     pass
# eagele = Eagle()
# # eagele.fly()  raise NotImplementedError 발생

class Duck(Bird):
    def fly(self):
        print("fly fast")

duck = Duck()
duck.fly()


"""
 9. except 만들기
 
 python 내장class인 Exception 이용
"""

class MyError(Exception):
    def __str__(self):
        return "not allowed nickname"

def say_nick(nick):
    if nick == 'yoda':
        raise MyError()
    print(nick)

say_nick("ronaldo")
# say_nick("yoda") error 발생

try:
    say_nick("messi")
    say_nick("yoda")
except MyError as e:
    print(e)


print("-" * 50)

class MyError2(Exception):
    def __int__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def say_name(name):
    if name == "yoda":
        raise MyError2("can't use this name")
    print(name)

try:
    say_name("rooney")
    say_name("yoda")
except MyError2 as e:
    print(e)