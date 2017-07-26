'''
Created on 2017-07-26 16:17

@ product name : PyCharm Community Edition

@ author : yoda
'''

f = open("test_movie.txt", "w", encoding="UTF-8")
f.write('''
현재 상영 영화 정보 best3

호날두
2000
짱
3000
메시
1000
''')
f.close()