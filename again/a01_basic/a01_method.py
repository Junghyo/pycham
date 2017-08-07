'''
Created on 2017-08-07 19:16

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns
import scipy as sp
import scipy.stats as stats

ex = """Your man on the road, he doing promo
You said keep our business on the low-low123"""

# len() : 문자열 길이
print(len(ex))  # 83

#  min(), max() : 문자열 내 문자, 혹은 숫자의 최소값, 최대값 (알파벳 순서, 숫자 순서 기반)
print(max(ex)) # w

# count() :  문자열 안에서 매개변수로 입력한 문자열이 몇 개 들어있는지 개수를 셈
# begin end 설정 가능
print(ex.count("a", 15, len(ex)))    # 2

# startswith() : 문자열이 매개변수로 입력한 문자열로 시작하면 True, 그렇지 않으면 False 반환
print(ex.startswith("a"))   # False
print(ex.startswith("Your"))   # True

# endswith() : 문자열이 매개변수로 입력한 문자열로 끝나면 True, 그렇지 않으면 False 반환
print(ex.endswith("a")) # F
print(ex.endswith("123")) # T

# find() : 문자열에 매개변수로 입력한 문자열이 있는지를 앞에서 부터 찾아 index 반환, 없으면 '-1' 반환
print(ex.find("y")) # -1
print(ex.find("a")) # 6

# rfind() : 문자열에 매개변수로 입력한 문자열이 있는지를 뒤에서 부터 찾아 index 반환, 없으면 '-1' 반환
print(ex.rfind("a"))    # 42

#  index() :  find()와 기능 동일하나, 매개변수로 입력한 문자열이 없으면 ValueError 발생

#  rindex() : index()와 기능 동일하나, 뒤에서 부터 매개변수의 문자열이 있는지를 찾음

# isalnum() : 문자열이 알파벳과 숫자로만 이루어졌으면 True, 그렇지 않으면 False
ex1 = 'I Love Python'
ex2 = 'abc'
ex3 = '123abc'
ex4 = '123'
ex5 = 123
print(ex1.isalnum())    # False 빈칸이 있기 때문
print(ex2.isalnum())    # True
print(ex4.isalnum())    # True

# isalpha() : 문자열이 알파벳(영어, 한글 등)으로만 이루어졌으면 True, 그렇지 않으면 False
print(ex1.isalpha())
print(ex2.isalpha())
print(ex3.isalpha())
print(ex4.isalpha())
# False
# True
# False
# False

# isdigit() : 문자열이 숫자만 포함하고 있으면 True, 그렇지 않으면 False, isnumeric()과 동일
# isnumeric() 동일
print(ex1.isdigit())
print(ex2.isdigit())
print(ex3.isdigit())
print(ex4.isdigit())
# False
# False
# False
# True

# lower() : 문자열 내 모든 대문자를 모두 소문자(a lowercase letter)로 변환
# upper() :  문자열 내 모든 소문자를 모두 대문자(a uppercase letter)로 변환
# swapcase() : 문자열 내 소문자는 대문자로 변환, 대문자는 소문자로 변환

# istitle() : 문자열이 제목 형식에 맞게 대문자로 시작하고 이후는 소문자이면 True, 그렇지 않으면 False
div()
ex1 = 'I Love Python'
ex2 = 'I LOVE PYTHON'
print(ex1.istitle())
print(ex2.istitle())
# True
# False

# title() : 문자열을 제목 형식(titlecased)에 맞게 시작은 대문자로, 나머지는 소문자로 변환
print(ex2.title())  # I Love Python

# capitalize() : 문자열 내 첫번째 문자를 대문자로 변환하고, 나머지는 모두 소문자로 변환
print(ex2.capitalize()) # I love python

# strip() : 문자열의 양쪽에 있는 공백을 제거
# lstrip() : 문자열의 왼쪽에 있는 공백을 제거
# rstrip() : 문자열의 오른쪽에 있는 공백을 제거

# center(width) : 총 길이가 매개변수로 받는 문자열폭(width)만큼 되도록 공백을 추가하여 중앙 정렬
print(ex2.center(30))   #         I LOVE PYTHON

# split() : 문자열을 구분자(delimiter, separator) 기준에 따라 나누기
ex1 = "hi, hello, nice"
print(ex1)
print(ex1.split(sep=","))
# hi, hello, nice
# ['hi', ' hello', ' nice']

# splitlines() : 여러개의 줄로 이루어진 문자열을 줄 별로 구분하여 리스트 생성
ex2 = """hi
hello
nice"""
print(ex2)
print(ex2.splitlines())
# hi
# hello
# nice
# ['hi', 'hello', 'nice']
ex3 = "hi\nhello\nnice"
print(ex3)
print(ex3.splitlines())
# hi
# hello
# nice
# ['hi', 'hello', 'nice']

# replace(old, new, max) : old 문자열을 new 문자열로 교체.
# 단, max 매개변수 있으면, max 개수 만큼만 교체하고 이후는 무시
print(ex1)
print(ex1.replace("l", "A"))
print(ex1.replace("l", "S", 1))
# hi, hello, nice
# hi, heAAo, nice
# hi, heSlo, nice

# join() :  여러개의 문자열을 구분자(separator) 문자열을 사이에 추가하여 붙이기
ex1 = ["a", "b", "c"]
print(ex1)
print("_".join(ex1))
# ['a', 'b', 'c']
# a_b_c

#  zfill(width) : 문자열을 매개변수 width만큼 길이로 만들되, 추가로 필요한 자리수만큼 '0'을 채움
ex1 = "aaa"
print(ex1.zfill(10))    # 0000000aaa

#  rjust(width[, fillchar]) : 문자열을 매개변수 width만큼 길이로 만들되, 오른쪽은 원본 문자열로 채우고,
# 왼쪽에 추가로 필요한 자리수만큼 매개변수 fillchar 문자열로 채움
# ljust()
print(ex1.ljust(20, "L"))
print(ex1.rjust(20, "R"))
# aaaLLLLLLLLLLLLLLLLL
# RRRRRRRRRRRRRRRRRaaa

