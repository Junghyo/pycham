'''
Created on 2017-07-27 10:53

@ product name : PyCharm Community Edition

@ author : yoda
'''
"""
 zip file 압축 zipfile모듈
 1. zipfile 함수로 압축객체 생성, write()함수를 이용해서
 하나씩 압축

 2. 압축해제 : zipfile을 만든 후, extractall()로 처리
"""


import numpy as np
import zipfile as zp
flist = ["test.txt", "test01.txt", "test02.txt",
         "test_movie.txt", "test_movie1.txt"]

with zp.ZipFile("compress.zip", "w", compression=zp.ZIP_BZIP2) as myzip:
    for temp in flist:
        myzip.write(temp)

# 압축해제 : extractall("경로설정")
# zp.ZipFile("compress.zip").extractall("경로설정")

"""
 tar file 압축은 tarfile 모듈
 
 1. open 함수를 이용해 압축객체 생성, add함수를 통해 파일추가가
 
 2. 압축해제 extractall() 호출
"""

import tarfile as tf
flist = ["a01_file.py", "a02_file_read.py", "a03_movie_write.py"]

with tf.open("tar_test.tar", "w:tar") as mytar:
    for temp in flist:
        mytar.add(temp)

# 압축해제
# tf.open("tar_test.tar").extractall("경로설정")