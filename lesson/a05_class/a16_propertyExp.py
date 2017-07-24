'''
Created on 2017. 7. 24.

@author: kitcoop
property와 private 선언 (확인예제)
Member 클래스 선언.
  id, pass는 private변수로 선언.
  setLoginId() == 통해서 저장 및 호출 처리.
  getLoginId()
  ==> goid변수로도 할당
  setLoginPass() 
  getLoginPass() 
  ==> gopass변수로도 할당.

  메서드 
  login(id, pass)
  를 통해서 현재 저장된 id와 pass가 맞는지
  여부를 "인증/미인증 처리

'''
from nt import getlogin
class Member:
    def __init__(self):
        self.__id1__="id저장되지 않음"
        self.__pass1__="password가 저장되지 않음"
        
    def setLoginId(self,id01):
        self.__id1__=id01
        
    def getLoginId(self):
        return self.__id1__

    
    def setLoginPass(self,pass01):
        self.__pass1__=pass01
        
    def getLoginPass(self):
        return self.__pass1__

    
    def login(self, id, pass01):
        isVal="미인증"
        if id=="himan" & pass01=="7777":
            isVal="인증"
        return isVal
    
    goId = property(setLoginId, getLoginId)  
    gopass= property(setLoginPass, getLoginPass)    
m01 = Member()
print("아이디:",m01.getLoginId())   
m01.goId="himan"     
print("아이디:",m01.getLoginId())        

    
    
    

    
           
        
        
        
        
        
        
        