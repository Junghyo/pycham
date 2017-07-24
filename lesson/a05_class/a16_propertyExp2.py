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
'''
class Member:
    def __init__(self):
        self.__id__="id저장되지 않음"
        
    def setLoginid(self,id01):
        self.__id__=id01
        
    def getLoginid(self):
        return self.__id__
    loginid = property(setLoginid, getLoginid)  

m01 = Member()

print("아이디:",m01.getLoginid())

m01.loginid="하이맨"  
print("아이디:",m01.getLoginid())
'''
class Member:
    def __init__(self):
        self.__id__="저장되지 않음"
        self.__pass__="저장된 않음"
    def getLoginid(self):
        return self.__id__
    def setLoginid(self,id):
        self.__id__=id 
    def getLoginpass(self):
        return self.__pass__
    def setLoginpass(self, pass01):
        self.__pass__=pass01        
    goid = property(getLoginid, setLoginid)     
    gopass = property(getLoginpass, setLoginpass)   
    
    def login(self,id,pass01):
        isvalid="미인증"
        if self.__id__ ==id and self.__pass__==pass01:
            isvalid="인증"
        return isvalid    
      
p01 = Member()
print(p01.getLoginid()) 
p01.goid="himan"
print(p01.getLoginid()) 
print(p01.getLoginpass()) 
p01.gopass="7777"
print(p01.getLoginpass()) 

print("인증데이터:",p01.login("himan", "7777"))
print("미인증데이터:",p01.login("himan", "7779"))
  
    

    
           
        
        
        
        
        
        
        