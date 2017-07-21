'''
Created on 2017. 7. 19.

@author: kitcoop
Tuple : 읽기 전용 - 리스트 보다 속도 빠름.
'''
t1 = "a", "b", "c","a"
t2 = ("a", "b", "c","a")
t3 = (1, 2, 3,4)
print(t1,t2)
print(t1, t1*2, len(t1), t1.count("a"), t1.index("b"))
print(t3, t3*2, len(t3))

p =(1,2,3)
# p[1]=20 수정 불가
''' 튜플데이터를 list으로 변경'''
q=list(p)
print(q)
q[1] = 20
print(q)
''' 형변환 '''
p = tuple(q)
print(p)

from urllib.parse import urlparse
a = 'http://www.naver.com:80/index.html'
print(a)
re = urlparse(a)
print(re)
print(re.netloc)

from urllib.parse import urlunparse
re2 = urlunparse(re)
print(re2)
