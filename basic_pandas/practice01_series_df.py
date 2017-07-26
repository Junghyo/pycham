'''
Created on 2017-07-26 15:49

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 pandas package
 
 Pandas 패키지는 데이터 분석을 할 때 가장 많이 쓰이는 패키지 중의 하나이다.
 대부분의 데이터는 시계열(series)이나 표(table)의 형태로 나타낼 수 있는데
 Pandas 패키지에서는 이러한 표 데이터를 다루기 위한 Series(Series) 클래스와
 DataFrame(DataFrame) 클래스를 제공한다.

"""

"""
 Series
 
 Series 클래스는 numpy에서 제공하는 1차원 배열과 비슷하지만
 각 데이터의 의미를 표시하는 index(index)를 붙일 수 있다.
 
 Series 생성
 
 데이터를 리스트나 1차원 배열 형식으로 Series 클래스 생성자에 넣어주면
 Series 클래스 객체를 만들 수 있다. index의 길이는 데이터의 길이와 같아야 한다.
 다음 예에서 이 "서울", "부산" 등의 문자열이 index의 값이다.
 index의 값을 index 라벨(label)이라고도 한다.
 index 라벨은 문자열 뿐 아니라 날짜, 시간, 정수 등도 가능하다.
"""
import numpy as np

import pandas as pd

from mymod.print import *

# ex) 각 도시의 2015년 인구 데이터를 series로 생성(index 설정)

# random값으로 인구수 설정해봄 (pandas + numpy)
# pop = pd.Series(np.random.random_integers(5000000, 9999999, 4),
#                 index=["Seoul", "Busan", "Incheon", "Daegu"])
pop = pd.Series([9904312, 3448737, 2890451, 2466052],
                index=["Seoul", "Busan", "Incheon", "Daegu"])
print(pop)
print(type(pop))    # <class 'pandas.core.series.Series'>


# index를 지정하지 않으면 0~ 정수값으로 설정된다.

print(pd.Series(range(10, 14)))

"""
 Series의 index는 index 속성으로 접근할 수 있다.
 Series의 값은 사실 numpy의 1차원 배열이며 values 속성으로 접근할 수 있다.
"""
print(pop.values)   # [9904312 3448737 2890451 2466052]
print(pop.index)    # Index(['Seoul', 'Busan', 'Incheon', 'Daegu'], dtype='object')

"""
 또한 Series 데이터는 name 속성을 이용하여 자체적인 이름을 붙일 수 있으며
 index.name 속성으로 index에도 이름을 붙일 수 있다.
"""
pop.name = "population"
pop.index.name = "city"

print(pop)
# city
# Seoul      9904312
# Busan      3448737
# Incheon    2890451
# Daegu      2466052
# Name: population, dtype: int64

"""
 Series 연산
 
 Series는 numpy 배열과 동일하게 벡터화 연산을 할 수 있다. 
 다만 연산을 해도 index 값은 변하지 않는다.
 예를 들어 인수를 백만 단위로 만들기 위해
 Series 객체 전체를 1,000,000 으로 나누어도 index 라벨에는
 영향을 미치지 않는 것을 볼 수 있다.
"""
print(pop/1000000) # value값만 연산


"""
 Series indexing, slicing
 
 또한 numpy 배열에서 가능한 index 방법이외에도 index 라벨을 이용한 indexing도 할 수 있다.
 배열 indexing이나 index 라벨을 이용한 슬라이싱(slicing)도 가능하다.
"""
print("=" * 50)
print("Series indexing, slicing")
print("=" * 50)


print(pop[1]) # index 위치로 해당 value return
print(pop["Daegu"])  # index name으로 해당 value return
print(pop.Seoul)  # index가 영문인 경우 이런식으로도 value값 return 가능

print(pop[[3, 1, 0]]) # 순서를 변경하거나 특정자료만 선택 가능
print(pop[["Incheon", "Busan"]])  # index name으로도 가능

# 250e4 ~ 500e4 이하 인구인 도시만 보고 싶으면?
print(pop[(250e4 <= pop) & (pop <= 500e4)])

# 문자열 index.name을 이용하여 slicing 하는 경우
# : 뒤에 오는 해당 index의 value도 포함된다.

print(pop[1:3])  # Busan, Incheon
print(pop["Busan":"Daegu"]) # Daegu도 포함됨


"""
 Series와 dict 자료형
 
 Series 객체는 라벨 값에 의해 indexing이 가능하므로 실질적으로
 라벨 값을 키(key)로 가지는 사전(dict) 자료형과 같다고 볼 수 있다.
 따라서 사전 자료형에서 제공하는 in 연산도 가능하고 iteritems 메서드를 사용하면
 for 루프를 통해 각 원소의 키(key)와 값(value)을 접근할 수도 있다.
"""
print("=" * 50)
print("Series like dict")
print("=" * 50)

print("Seoul" in pop)   # True
print("Seoul" not in pop)   # False

for k, v in pop.iteritems():
    print("%s = %d" % (k, v))

# Seoul = 9904312
# Busan = 3448737
# Incheon = 2890451
# Daegu = 2466052

print(pop.keys())
print(pop.index)
# Index(['Seoul', 'Busan', 'Incheon', 'Daegu'], dtype='object', name='city')
# 동일하게 출력

print(pop.index.values)  # print(pop.index.values)

print(pop.values)   # [9904312 3448737 2890451 2466052]

print(pop.index.name)  # city
print(pop.name) # population

"""
 dict 객체로 Series를 만들 수 있다.
"""

pop_dict = {"Seoul": 9631482, "Busan": 3393191, "Incheon": 2632035, "Daejeon": 1490158}
print(pop_dict)
print(pop_dict.keys())
print(pop_dict.values())
print(pop_dict.items())
# {'Seoul': 9631482, 'Busan': 3393191, 'Incheon': 2632035, 'Daejeon': 1490158}
# dict_keys(['Seoul', 'Busan', 'Incheon', 'Daejeon'])
# dict_values([9631482, 3393191, 2632035, 1490158])
# dict_items([('Seoul', 9631482), ('Busan', 3393191), ('Incheon', 2632035), ('Daejeon', 1490158)])

# dict를 Series를 변환
pop2 = pd.Series(pop_dict)
print(pop2)

# 변환시 순서를 보장해주지 않으므로 순서를 정하고 싶다면 index 설정
pop2 = pd.Series(pop_dict, index=["Busan", "Seoul", "Incheon", "Daejeon"])
print(pop2)
print(type(pop2))   # <class 'pandas.core.series.Series'>

"""
 index 기반 연산
 
 연산을 하는 경우 index가 같은 데이터끼지 알아서 차이를 구해 준다.
 즉 index 기반으로 연산을 한다.
"""

print(pop-pop2) # index값 순서가 달라도 알아서 차이를 구해줌

gap = pop - pop2

# boolean 값으로 표시
print(gap.notnull())

# NaN이 아닌 data만 return
print(gap[gap.notnull()])

# 인구 증가율 구하기
roi = (pop - pop2) / pop2 * 100
roi = roi[roi.notnull()]
print(roi)

"""
 data update, add, delete
"""
div()

roi.Busan = 1.63 # Busan data값 update
print(roi)

div()

roi["Daegu"] = 1.41
print(roi)

# 삭제시 del 사용

del roi["Seoul"]
print(roi)

"""
 DataFrame class
 
 Series가 1차원 벡터 데이터에 행방향 index(row index)를 붙인 것이라면
 DataFrame 클래스는 2차원 행렬 데이터에 index를 붙인 것과 비슷하다.
 2차원이므로 행방향 index(row index) 뿐 아니라 열방향 index(column index)도 붙일 수 있다.
"""

"""
 DataFrame 생성
 
 DataFrame을 만드는 방법은 다양하다.
 가장 간단한 방법은 다음과 같이 리스트나 일차원 배열을 값(value)으로 가지고
 열방향 index 라벨을 키(key)로 가지는 사전(dictionary) 데이터를
 DataFrame 클래스 생성자에 넣는다. 
 이 때 열방향 index는 columns 인수에, 행방향 index는 index 인수에 지정한다.
"""
div()

data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}

col = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
index = ["서울", "부산", "인천", "대구"]
df = pd.DataFrame(data, index=index, columns=col)
s1 = pd.Series(data, index=col) # Series로 만들어봄.
print(df)

"""
앞에서 DataFrame은 2차원 배열 데이터를 기반으로 한다고 했지만
사실은 동일한 index를 가지는 열 Series(column series)를
사전(dictionary)처럼 묶어놓은 것이라고 보는 것이 더 정확하다.
2차원 배열 데이터는 모든 원소가 같은 자료형을 가져야 하지만
DataFrame은 각 열(column)마다 자료형이 다를 수 있기 때문이다.
위 예제에서도 지역과 인구와 증가율은 각각 문자열, 정수, 부동소수점 실수이다.
"""

"""
Series와 마찬가지로 데이터만 접근하려면 values 속성을 사용한다.
열방향 index와 행방향 index는 각각 columns, index 속성으로 접근한다.
"""
div()

print(df.values)

# 컬럼명 return
print(df.keys())
print(df.columns)
# Index(['지역', '2015', '2010', '2005', '2000', '2010-2015 증가율'], dtype='object')

print(df.ndim) # 2차원
print(df.shape) # 4행 6열

# 행 이름
print(df.index)
# Index(['서울', '부산', '인천', '대구'], dtype='object')

# Series 처럼 열방향 index(colums)와 행방향 index에 name 설정 가능
df.index.name = "도시"
df.columns.name = "특성"
print(df)

"""
 DataFrame 열 indexing
 
 DataFrame을 indexing을 할 때도 열 라벨(column label)을 키값으로 생각하여 indexing을 할 수 있다.
 index로 라벨 값을 하나만 넣으면 Series 객체가 반환되고 라벨의 배열 또는 리스트를 넣으면
 부분적인 DataFrame이 반환된다.
"""
div()

print(df["지역"])
print(df[["2015", "2005"]]) # 두개 컬럼 동시에 보기

div()
print(df["2010"])
div()
print(df[["2010"]])
div()
print(df["2010"]["서울"])  # 2010년도 서울 인구수 9631482

print(type(df["2010"])) # <class 'pandas.core.series.Series'>
print(type(df[["2010"]]))   # <class 'pandas.core.frame.DataFrame'>


"""
 df[0], df[[0]]
 
 DataFrame의 열 index가 문자열 라벨을 가지고 있는 경우에는
 순서를 나타내는 정수 index를 열 indexing에 사용할 수 없다.
 정수 indexing의 슬라이스는 행(row)을 indexing할 때 사용하므로
 열을 indexing할 때는 쓸 수 없다.
"""
df2 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df2)

# 문자열로 된 열 label이 없는 경우 정수 사용 가능
print(df2[0])   # Name: 0, dtype: int32
print(df2[2])   # Name: 2, dtype: int32

print(df2[1][2]) # DataFrame은 조회할 때 열, 행 index순으로 해야 하는 듯?


"""
 columns data - update, add, delete
 
 DataFrame은 열 Series의 사전으로 볼 수 있으므로
 열 단위로 데이터를 갱신하거나 추가, 삭제할 수 있다.
"""
div()

print(df)

# 수정
df["2010-2015 증가율"] = df["2010-2015 증가율"] * 100
print(df)

# 추가
df["2005-2010 증가율"] = ((df["2010"] - df["2005"]) / df["2005"] * 100).round(2)
# 소수점 2자리에서 반올림

print(df)

# 삭제
del df["2010-2015 증가율"]
print(df)


"""
 개별 data값 indexing
 
 
DataFrame에서 열 라벨로 Series를 indexing하고
다시 행 라벨로 개별 데이터를 indexing할 수 있다.
"""
div()

print(df)

# 서울의 2010 인구수 찾기
print(df["2010"]["서울"])
print(df["2010"][0])
# 9631482 동일한 값

"""
 행 단위 indexing
 
 만약 행 단위로 인덱싱을 하고자 하면 항상 슬라이싱(slicing)을 해야 한다.
 시리즈와 같이 라벨 슬라이싱도 가능하다.
 행 단위는 숫자로 이용 가능
"""
# 서울의 값만 보려고 한다면?
# print(df[0]) 불가
print(df[:1])

# 부산을 보려고 한다면?
print(df[1:2])
# 서울을 빼고 보려고 한다면?
print(df[1:])
# index명으로도 가능
print(df["서울":"대구"]) # index명으로 조회할 경우, : 뒤의 index 해당 값까지 포함.

# 대구(마지막 행)을 제외하고 보려고 한다면?
print(df[:-1])

"""
연습 문제 1

원하는 자료를 기반으로 두 개의 시리즈 객체를 만들어 본다.
문자열 인덱스를 가져야 하며 두 시리즈에 공통적으로 포함되지 않는 라벨이 있어야 한다.
두 시리즈 객체를 이용하여 연산을 한다.
"""
div()

s = pd.Series(range(1, 6), index=["a", "b", "c", "d", "e"])
print(s)
s.name = "number"
s.index.name = "alphabet"
print(s)

print(s[1])
print(s["b"])
print(s.b)
# 전부 2

s1 = pd.Series(range(10, 60, 10), index=["b", "a", "f", "w", "d"])
tot = s1 + s
print(tot)
print(tot[tot.notnull()])
print(tot[tot > 12])

"""

연습 문제 2

각자 원하는 데이터로 데이터프레임을 만든다. 단 다음 조건을 만족해야 한다.
열의 갯수와 행의 갯수가 각각 5개 이상이어야 한다.
열에는 정수, 문자열, 실수 자료형 데이터가 각각 1개 이상씩 포함되어 있어야 한다
"""
div()

df1 = pd.DataFrame(np.arange(1, 10).reshape(3, 3),
                   index=["row1", "row2", "row3"],
                   columns=["col1", "col2", "col3"])
print(df1)

data = {"col1": [10, 40, 70], "col2": [20, 50, 80], "col4": [30, 60, 90]}

df2 = pd.DataFrame(data, index=["row1", "row2", "row3"])
print(df2)

# 연산 가능
tot = df1 + df2
print(tot)
print(tot.notnull())

# numpy 이용하여 각 행 및 열 곱셈 가능
print(np.prod(tot, axis=1)) # 행 곱셈
print(np.sum(tot, axis=0))  # 열 덧셈
