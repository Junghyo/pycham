'''
Created on 2017. 7. 24.

@author: kitcoop
try:
    #코드블록1
except:
    #코드블록1에서 예외가 발생했을 때..
else:
    #코드블록1이 예외가 발생하지 않았을 때..
finally:
    #코드블록1에서 예외가 발생했건, 하지 않았건
    처리할 내용
'''
list=[1,2,3]

print(list)

try:
    index = int(input("인덱스번호를 입력하세요!!"))
    print(list[index])
except IndexError as err:
    print("잘못된 index 입니다:({0})".format(err))    
else:
    print("리스트의 요소 출력에 성공햇습니다!")
finally:
    print("무조건 수행")
    
    