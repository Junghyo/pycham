'''
Created on 2017. 7. 21.

@author: kitcoop
확인예제
shopping
    가격과 갯수를 입력 받아서..
    쇼핑한 총 비용을 계산 처리하세요..

1. 함수를 이용
2. 람다 이용
'''
def shopping(price, cnt):
    return price*cnt

prices =[2000,3000,4000]
cnts =[2,3,2]
print("함수이용")
pays = list(map(shopping,prices,cnts))
print("합산금액들:",pays)
print("총계:",sum(pays))
print("람다이용")
pays2 = list(map(lambda price, cnt:price*cnt, prices, cnts));
print("합산금액들:",pays2)
print("총계:",sum(pays2))


