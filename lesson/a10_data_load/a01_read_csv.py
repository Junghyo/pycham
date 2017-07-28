'''
Created on 2017-07-28 13:10

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 read csv file
 1. pandas.read_csv("filepath"), pandas.read_table("filepath")
 
 2. read_csv 기본 구분자(,)
    read_table 기본 구분자 tab

 csv
 pandas.read_csv()
 1. sep: 구분자 설정
 2. header: 컬럼이름
 3. index_col: 인덱스로 사용할 번호나 이름 또는 리스트
 4. names: 컬럼이름으로 사용할 번호나 이름 또는 리스트
 5. skiprows: 읽지 않을 행의 숫자
 6. na_values: 특정값을 NaN으로 변환
 7. comment: 주석으로 분류되어 파싱하지 않을 문자
 8. converters: 변환 시 컬럼에 적용할 함수 지정
 9. norws: 파일의 일부분만 읽어올 때
 10. skip_footer: 무시할 마지막 줄 수
 12. squeeze: 로우가 하나뿐. Series 객체 반환
 13. thousands: 숫자를 천단위로 끊을 때
"""
items = pd.read_csv("item.csv")
print(items)

# goods = pd.read_csv("good.csv", header=None, names=["제품명", "갯수", "가격"])
# print(goods)

goods = pd.read_csv("good.csv",
                    header=None,
                    names=["제품명", "갯수", "가격"],
                    thousands=",")
print(goods)

# 갯수의 누적 합 : cumsum()
div()

print(goods["갯수"].cumsum())

# 요약
print(round(goods.describe(), 2))


"""
emp.csv 만들기
사번, 이름, 부서번호, 급여 (data 5개)

1. 컬럼명 설정

2. 시작 row를 두번째부터

3. 마지막 2개 데이터 생략
"""
f = open("emp.csv", "w", encoding="UTF-8")
f.write("""
사번, 이름, 부서번호, 급여
1,  lee,    10, 3000
2, kim, 20, 2000
3, hong, 30, 1500
4, park, 20, 4500
5, seo, 10, 9999
""")
f.close()

# 1. 컬럼명 설정
df = pd.read_csv("emp.csv", skiprows=2, names=["empno", "name", "deptno", "sal"])
print(df)

# 2. 시작 row를 두번째부터
df = pd.read_csv("emp.csv", skiprows=3, names=["empno", "name", "deptno", "sal"])
print(df)

# 3. 마지막 2개 데이터 생략
df = pd.read_csv("emp.csv", skiprows=2,
                 names=["empno", "name", "deptno", "sal"],
                 skipfooter=2, engine='python')
print(df)