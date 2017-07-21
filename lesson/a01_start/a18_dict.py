'''
Created on 2017. 7. 20.

@author: kitcoop

dict
 형식 :  dict(키1:데이터값1, 키2:데이터값2)
 key와 value값을 쌍으로 자료형
 key는 순서X, key값은 중복될 수 없다.
 하나씩 접근 시, 디셔너리이름[키] 
     ==> 키에 매핑되어 있는 데이터값을 return
 하나씩 데이터 할당.. 딕션너리이름[key]= 할당할 데이터..
     해당 key가 있을 때는 수정, 해당 key값 없을 때는 추가.
 없는 키를 호출하면 에러..
 키의 갯수 len(딕션너리이름)
 del 딕션너리이름[key] : 해당 딕션너리의 키와 값을 삭제     

'''
member ={"baseball":9,"soccer0":11,"volleyball":6}
print(member)
print("키로 데이터 접근(member['volleyball']):", member["volleyball"])

mydic = dict(k1=1, k2="abc",k3=3.4)
print(mydic)
dic = {'파이선':"뱀", "자바":"커피", "스프링":"용수철"}
print(dic)
print("길이:", len(dic))
print("자바key값 확인:", dic["자바"])
'''
 없는 key값 호출시에는 에러 발생
 index라고 믿는 key값으로 접근이 안됨 에러 발생
'''
##print("없은 key값 호출:", dic["커피"])
##print(dic[0])
'''
데이터 추가..
 딕션너리이름['키' ] = 할당할 데이터..
데이터 하나 삭제..
del 딕션너리이름[키]
전체 딕션너리 제거..
clear()

'''
dic["오라클"]  = "예언자"
print(dic)
del dic['스프링']
print(dic)
dic.clear()
print("삭제 후:",dic)

friends={"boy":"한국인","girl":"한송이","guy":"손오공"}
print(friends)
print(friends["girl"])
'''
전체 key 호출 : keys()
전체 valus 호출 : values()
'''
print("친구의 모든 key호출:",friends.keys())
print("친구의 모든 values호출:", friends.values())
'''
없는 키를 호출하니, 에러 발생..
 키 in 딕션너리이름..  = bool값으로 return
'''
print("boy" in friends)
print("mother" in friends)
'''
loop friends에 있는 key() 출력..
for 단위 객체 in 딕션너리이름.keys()
    print(단위객체, end="단위당 구분자")
'''
for k in friends.keys():
    print(k, end=" ")
print()    
for v in friends.values():
    print(v, end="\t")   
    







