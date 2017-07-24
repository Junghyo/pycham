'''
Created on 2017. 7. 24.

@author: kitcoop
'''
class MyException(Exception):
    def __init__(self, msg):
        super().__init__("예외발생.", msg)


try:
    inputNum = input("숫자를 입력하세요![1~10]")
    if inputNum.isdigit() == False:
        raise Exception("예외를 발생합니다!!숫자를 입력하세요!")
    inputNum = int(inputNum)
    if inputNum <= 0 or inputNum > 10:
        raise MyException("숫자는 0~10까지만 입력")

    print("입력한 숫자:", inputNum)
except  MyException as err1:
    print("예외가 발생했습니다(My)!!@@:", err1)
except  Exception as err2:
    print("예외가 발생했습니다!!@@:", err2)
