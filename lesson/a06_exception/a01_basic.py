'''
Created on 2017. 7. 24.

@author: kitcoop
'''
def func(y):
    x = input("숫자를 입력하세요")
    return int(x)**y

try:
    print(func(5))
    ## 예외를 강제적으로 문자열을 입력함으로 발생..
except: ## 예외가 발생했을 때, 처리할 block
    print("예외가 발생 했습니다!!")    
##예외가 발생하지 않았을때, 처리할 block
else:
    print("예외가 발생하지 않고 정상처리 되었습니다.")     
