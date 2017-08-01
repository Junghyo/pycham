'''
Created on 2017-08-01 14:35

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import pytagcloud
from collections import Counter

foods = list()
foods.extend(["피자" for i in range(8)])
foods.extend(["초밥" for i in range(5)])
foods.extend(["짬뽕" for i in range(3)])
foods.extend(["탕수육" for i in range(1)])
foods.extend(["삼겹살" for i in range(4)])
foods.extend(["짜장면" for i in range(12)])
foods.extend(["김치찌개" for i in range(7)])
foods.extend(["우동" for i in range(5)])
foods.extend(["우동" for i in range(2)])
foods.extend(["우동" for i in range(7)])
foods.extend(["우동" for i in range(4)])
# 데이터 건수 확인
count = Counter(foods)
print(count)
tag2 = count.most_common(100)
taglist = pytagcloud.make_tags(tag2, maxsize=50)
print(taglist)

# wordcloud
pytagcloud.create_tag_image(taglist, "wordscloud.jpg",
                            size=(900, 600), fontname="Korean", rectangular=False)