'''
Created on 2017. 7. 19.

@author: kitcoop
'''
print("몇번 반복할까요?:")
limit = int(input())

count=0
while count < limit:
    count = count +1
    print("{0}회 반복".format(count))

print("반복이 종료 되었습니다!")    