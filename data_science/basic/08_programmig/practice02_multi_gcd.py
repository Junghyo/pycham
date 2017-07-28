'''
Created on 2017-07-24 20:30

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다.
이들의 총합은 23이다.
1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
"""

def ex(y):
    result = 0
    for x in range(1, y):
        if x % 3 == 0 or x % 5 == 0:
            result += x
    return result

print(ex(1000))

"""
 최대 공약수(gcd)
 ex) 18 , 12의 최대 공약수
 18 / 12 = 몫 1  나머지 6
 12 / 6 = 0
 6 최대 공약수

 최소공배수(lcm)
  a * b / gcd
"""



def gcd2(m, n):
    while n != 0:
        t = m % n
        (m, n) = (n, t)
    return abs(m)



def gcdlcm(a, b):
    answer = []
    gcd = lambda a, b : a if not b else gcd(b, a % b)
    lcm = int(a * b / gcd(a, b))
    answer = [gcd(a, b), lcm]
    return answer

gcd = lambda a, b : a if not b else gcd(b, a % b) # 최대공약수
lcm = int(a * b / gcd(a, b)) # 최소공배수

print(gcd(78696, 19332))


print(gcdlcm(78696, 19332))

print(gcdlcm(12, 18))