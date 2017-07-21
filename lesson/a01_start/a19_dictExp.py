'''
Created on 2017. 7. 20.

@author: kitcoop
확인예제
좋아하는 영화
  영화제목, 관람한 날짜, 함께한사람

1. dic으로 위 내용을 객체로 만들고,
2. for 구문을 통해 value값을 구분자 @로 출력
3. 지불비용을 key와 value값으로 등록
4. 함께한사람의 key로 value값으로 출력
5. 영화제목을 key 있는지 여부를 
   bool으로 확인해서, 영화제목을 변경 처리.

'''
favmovie ={"title":"늑대와 춤을", "viewdate":"1991.4.5","together":"좋은친구1"}
print(favmovie)
for val in favmovie.values():
    print(val, end="@")
print()    
favmovie['pay']=5000
print(favmovie)
print(favmovie['together'])
if 'title' in favmovie :
    favmovie['title'] = "백투더퓨처3"   
print(favmovie)    

