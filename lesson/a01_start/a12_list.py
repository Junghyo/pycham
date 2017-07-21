'''
Created on 2017. 7. 19.

@author: kitcoop

List : 순서 있고, 값 변경 가능..
'''
from audioop import reverse
list01 =[1,2,3]
list02 =[10,list01,20.5,True, "문자열"]
print(list01)
print(list02)
print("메모리 위치list01:", id(list01))
print("메모리 위치list02:", id(list02))
print()
'''
 데이터 문자열 할당
'''
family =["아버지","어머니","나","형","남동생","여동생"]
print(family) 
'''
len(list형)
'''
print("가족수는:", len(family),"명")
print("서열2위(index 1):", family[1])
'''
메서드 활용하여 추가하기..
.append(추가될 내용)
'''
family.append("누나")
print(family)
'''
삭제처리 .remove("대상")
'''
family.remove("나")
print(family)
'''
특정 위치에 해당한 내용 추가..
insert(위치 index, 추가할 내용)
'''
family.insert(0, "할아버지")
print(family)
'''
list를 확장.. extend(list내용)
+(연산기호를 통해 동일한 처리 가능)
'''
family.extend(["삼촌","조카"])
print(family)

family+=["이모"]
print(family)
'''
특정 위치 있는 index 내용 return
'''
print(family.index("남동생"))
'''
해당 데이터 여부에 대한 확인..
검색 in list 데이터...
'''
print("어머니" in family, "나" in family)

'''
슬라이싱
'''
numList =[1,2,3,4,5]
print(numList[0:2])
numList.insert(3, ["홍길동","김길동","신길동"])
print(numList)
numList[0]=100 
''' 특정 위치 데이터 변경 가능 '''
'''
    index 3번째,  첫번째 데이터 변경..
'''
numList[3][0]="변길동"
print("변경 후 확인:", numList)
'''
3번째에서 배열을 리스트
'''
print(numList[3][:1])
'''
특정 데이터도..
'''
numList[3].remove("신길동")
print(numList)
numList=[2,5,2,2,1]
numList.sort()
print(numList)
''' 역정렬 처리..
'''
numList.sort(reverse=True)
print(numList)

'''
메트릭스 사용 하기..
'''
matrix01 =[[1,2,3],[4,5,6],[7,8,9]]
print(matrix01[1][1])
'''
문자열 분리 후, 리스트에 저장
'''
chars=[]
sentence = "대한민국은 korea"
for k in sentence:
    chars.append(k)
    
print(chars)    
'''
복사 . 얕은 복사 : 주소 치환
'''
name01 ="홍길동"
name02 = name01
print(name01, name02)
print(id(name01), id(name02))
name01="수잔"
print(name01, name02)
print(id(name01), id(name02))
'''
복사 배열을 통한 얕은 복사 :주소 치환
'''
name = ["톰","제임스","찰스"]
name2 = name
print(name, name2)
print(id(name), id(name2))
name[0]="수잔"
print(name, name2)

'''
복사 깊은 복사 - 새로운 객체 생성
'''
import copy
name3 = copy.deepcopy(name) #새로운 객체 생성
print(name3)
name[0]="앨리스"
print(name, name2, name3)
print(id( name) , id( name2), id(name3))
'''
리스트로 stack(LIFO) 처리
'''
print("리스트로 stack(LIFO) 처리")
sbs =[10,20,30]
sbs.append(40)
print(sbs)
sbs.pop(); print(sbs)
sbs.pop(); print(sbs)
'''
리스트로 queue[FIFO] 처리
'''
print("리스트로 queue[FIFO] 처리")
sbs=[10,20,30]
sbs.append(40)
print(sbs)
sbs.pop(0); print(sbs)
sbs.pop(0); print(sbs)

def strlen(st):
    return len(st)
data =["Morning","Evening", "Afternoon","Nigth"]
data.sort(key=strlen)
print(data)









