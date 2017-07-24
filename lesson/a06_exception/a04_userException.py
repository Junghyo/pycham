'''
Created on 2017. 7. 24.

@author: kitcoop
'''
class MyException(Exception):
    def __init__(self,msg):
        super().__init__("MyException을 발생했습니다.",msg)

 
try:  
    print("데이터처리1")      
    print("데이터처리2")
    raise MyException("사용자 정의 예외 던짐!!")
except MyException as myerr :
    print("예외가 일어 났습니다!!{0}".format(myerr))       