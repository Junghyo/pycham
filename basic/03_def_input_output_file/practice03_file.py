'''
Created on 2017-07-20 18:05

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 write and read file
 
 파일 객체 = open(파일 이름, 파일 열기 모드)
 
 
 파일열기모드     	설명
 r	읽기모드         파일을 읽기만 할 때 사용
 w	쓰기모드         파일에 내용을 쓸 때 사용
 a	추가모드         파일의 마지막에 새로운 내용을 추가 시킬 때 사용 
"""

# # file 폴더에 new.txt 생성하기
# f = open("C:/pycharm/basic/file/new.txt", "w")
# f.close()
#
# # file 생성 및 출력값 작성하기
# f = open("C:/pycharm/basic/file/new.txt", "w")
# for i in range(1, 10):
#     data = "%i번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
#

# 외부 파일 읽기
# readline() : 첫번째 줄만 읽기
print("=" * 50)
print("readline()")
print("=" * 50)

f = open("C:/pycharm/basic/file/new.txt", "r")
line1 = f.readline()  # 첫번째 줄만 읽기
print(line1)
f.close()

# 모든 line을 읽고 싶다면
f = open("C:/pycharm/basic/file/new.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# input의 경우
while True:
    data = input()
    if not data: break
    print(data)

# data나 line이 없을 때까지 무한 loop를 돌면서 logic을 처리한다.


# readlines() : 모든 라인을 읽어서 각각의 줄을 element로 list 처리
print("=" * 50)
print("readlines()")
print("=" * 50)

# readline()의 경우
f = open("C:/pycharm/basic/file/new.txt", "r")
line = f.readline()
f.close()
print(line) # 1번째 줄입니다.

# readlines()의 경우
f = open("C:/pycharm/basic/file/new.txt", "r")
line = f.readlines()
f.close()
print(line)
# ['1번째 줄입니다.\n', '2번째 줄입니다.\n', '3번째 줄입니다.\n', '4번째 줄입니다.\n', '5번째 줄입니다.\n', '6번째 줄입니다.\n', '7번째 줄입니다.\n', '8번째 줄입니다.\n', '9번째 줄입니다.\n']

f = open("C:/pycharm/basic/file/new.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()


# read() 함수 이용하기 :
print("=" * 50)
print("read()")
print("=" * 50)

f = open("C:/pycharm/basic/file/new.txt", "r")
line = f.read()
print(line)
print(type(line))
f.close()
# 1번째 줄입니다.
# 2번째 줄입니다.
# 3번째 줄입니다.
# 4번째 줄입니다.
# 5번째 줄입니다.
# 6번째 줄입니다.
# 7번째 줄입니다.
# 8번째 줄입니다.
# 9번째 줄입니다.
# <class 'str'>

# 각각의 줄을 list의 element로 하여 list 만들기
line_list = line.split("\n")
print(line_list)
print(type(line_list))
# ['1번째 줄입니다.', '2번째 줄입니다.', '3번째 줄입니다.', '4번째 줄입니다.', '5번째 줄입니다.', '6번째 줄입니다.', '7번째 줄입니다.', '8번째 줄입니다.', '9번째 줄입니다.', '']
# <class 'list'>
