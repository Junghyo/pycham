'''
Created on 2017. 7. 21.

@author: kitcoop
클래스 : CoffeeShop
멤버 변수 : 
   커피종류
   가격
   주문수량
생성자를 통해서 : 커피종류를 등록처리
메서드
   order를 통해서 가격과 주문수량
   calc를 통해서 주문된 커피, 가격, 주문수량 출력.
'''
class CoffeeShop :
    price = 0
    cnt = 0
    def __init__(self, kind):
        self.kind = kind
    
    def order(self, price, cnt):
        self.price = price
        self.cnt = cnt
    
    def calc(self):
        print("## 주문된 커피 ##")
        print("커피 종류:",self.kind)
        print("커피 가격:",self.price)
        print("커피 수량:",self.cnt)
        print("총비용:",(self.price*self.cnt))

cs01 = CoffeeShop("모카라떼")
cs01.order(4000, 3)
cs01.calc()
         
        
    
