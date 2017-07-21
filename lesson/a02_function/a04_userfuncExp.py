'''
Created on 2017. 7. 20.

@author: kitcoop
'''
def exam(num01, num02):
    print(str(num01)+" + "+str(num02)+" = ?")
    indata = int(input("정답을 입력하세요!:"))
    return num01+num02 == indata

if exam(5,6):
    print(" good job")
else :
    print(" let's try it again!")    