'''
Created on 2017. 7. 20.

@author: kitcoop

set() : 순서, 중복X - 멤버검사, 중복자료 제거 유용



'''
hashset = set()
##print("초기값?:"+hashset)
hashset ={1,2,3}
print(hashset)
'''
튜블형식의 데이터  ()를 set으로 할당하여,
중복을 제거 처리...
'''
hashset = set((1,2,3,2))
print(hashset)
hashset = set('hello world')
print(hashset)
hashset = set([1,3,2])
print(hashset)
'''
여러가지 함수 활용하기..
추가 add(데이터), update([데이터 나열])
복사 copy()
전체 제거  clear()
한개 제거 discard(데이터) - 없으면 그냥 통과..
한개 제거 remove(데이터) - 없으면 예외 
pop() : 1개제거.(앞, 뒤에 내용 제거)
'''
a ={1,2,3,1}
print("갯수:",len(a))
b ={3,4}
'''
union() : 합집합 - 중복제거
intersection :교집합
'''
print(a.union(b))
print(a.intersection(b))
'''
연산자를 통한 데이터 처리
'''
print(a - b, a|b, a&b)
'''
set() index 접근?
'set' object does not support indexing
'''
##print(b[0])
b.add(5)
print(b)
'''
update()를 통하여 여러형식의 데이터를 추가
'''
b.update({6,7}) #set
print(b) 
b.update([7,8]) # list
print(b)
b.update((9,10)) # tuple
print(b)
'''
 데이터 삭제..
 discard()
 remove() : 없는 내용 삭제시, 에러발생..
'''
b.discard(7)
print(b)
b.discard(7)
print("동일내용 삭제(discard):",b)
b.remove(8)
print(b)
##b.remove(8)
##print("동일내용 삭제(remove):",b)
'''
할당과 형변환
clear() :전체삭제
'''
c = set()
c = b
print(c)
c.clear()
print("삭제후:",c)
print("형변환")
print("튜플형태로:", tuple(a))
print("리스형태로:", list(a))
'''
list의 데이터를 set으로 변환하여 중복제거후,
다시 list로 사용..
'''
li =[1,2,2,3,1]
s = set(li)
li = list(s)
print(li)

















