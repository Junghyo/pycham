'''
Created on 2017. 7. 24.

@author: kitcoop
'''
class Book:
    price = 3000
   
    @classmethod
    def showBookPrice(cls):
        print("가격:",cls.price)
    
    @staticmethod
    def showBookName():
        name = "알찬 빅데이터"
        print("도서명:",name)
