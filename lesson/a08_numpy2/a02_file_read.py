'''
Created on 2017-07-26 16:07

@ product name : PyCharm Community Edition

@ author : yoda
'''

f = open("test.txt", "r", encoding="UTF-8")
print(f)

# 한번에 전부 읽기 : read()
# print(f.read())
#
# # 첫째 줄만 읽기
# print(f.readline())

# 줄단위로 일기



# for l in f:
#     print(l)

# txt 줄단위로 list 만들기

txt = f.read()

txt_l = txt.split("\n")
print(txt_l)


"""
 ex) 
 write
 현재 상영 영화 정보 best 3
 제목 1
 관람료1
 제목 2
 관람료2
 제목 3
 관람료3
 test_move.txt
"""