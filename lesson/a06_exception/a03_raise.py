'''
Created on 2017. 7. 24.

@author: kitcoop
강제 예외발생

'''
try:
    print("출력1")
    print("출력2")
    text = input("숫자를 입력하세요1!")
    if text.isdigit() == False:
        raise Exception("예외를 발생합니다!!\n숫자를 입력하세요")
    print("입력된 숫자:", text)
except Exception as err :
    print("예외가 발생했습니다!!:{0}".format(err))    

