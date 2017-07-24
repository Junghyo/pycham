'''
Created on 2017. 7. 24.

@author: kitcoop
a05_class.Student
'''
class Student :
    no = 25
    ## 클래스 메서드 선언
    @classmethod
    def cmethod(cls):
        print("클래스 메서드")
        print(cls)
        print("학생번호:",cls.no)
    ## static 메서드 선언
    @staticmethod
    def smethod():
        print("정적 메서드")

   
   
