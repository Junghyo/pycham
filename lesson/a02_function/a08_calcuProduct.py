'''
Created on 2017. 7. 20.

@author: kitcoop

확인예제(람다형식으로 처리)
물건의 가격과 갯수를 입력 받아 총계처리(람다형식) 하세요..
일반 함수 : 물건명 가격 갯수
             @@@@   @@  @@
'''

tot = lambda price,cnt:price*cnt
def prodsell(name, price, cnt=0):
    print("물건명\t가격\t개수\t계")
    print(name,"\t",price,"\t",cnt,"\t",tot(price,cnt))
prodsell("사과",3000,2)  
    