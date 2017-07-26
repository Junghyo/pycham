'''
Created on 2017-07-26 15:53

@ product name : PyCharm Community Edition

@ author : yoda
'''

# open("파일명", "w-쓰기옵션", encoding= )
f = open("test.txt", "w", encoding="UTF-8") # utf-8로 encoding
print(f)    # <_io.TextIOWrapper name='test.txt' mode='w' encoding='UTF-8'>

f.write("만나서 반갑습니다.")
f.write("Nice to meet you.") # write()를 따로 사용해도 한줄에 그대로 출력됨
f.write("\n\n")

# 데이터를 줄 단위로 작성
lines = ["내 이름은 호날두다.", "My name is Ronaldo.", "호날두 짱", "Ronaldo awesome"]
# write("데이터구분자".join(배열데이터))
f.write("\n".join(lines))