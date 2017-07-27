'''
Created on 2017-07-27 09:48

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 바이너리 파일 : 바이트 단위로 데이터를 읽고 쓰는 것
 
 문자열을 기록할 수 없고, byte단위로만 기록
 문자열의 경우 encode 함수를 이용해서 byte로 변형
 바이트를 문자열로 변환할 떄는 decode 함수 이용
"""
import numpy as np

f = open("test02.txt", "wb")
f.write("안녕하세요".encode())
f.close()

f = open("test02.txt", "rb")
txt = f.read()
# print(txt)  TypeError: a bytes-like object is required, not 'str'
print(txt.decode())

