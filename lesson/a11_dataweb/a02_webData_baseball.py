'''
Created on 2017-07-31 17:28

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

# import
import requests as rq
from lxml.html import parse
import io

url = "http://www.koreabaseball.com/TeamRank/TeamRank.aspx"

data = rq.get(url)

doc = parse(io.StringIO(data.text))

root = doc.getroot()

table = root.findall(".//table")

# 제목(컬럼명)
title = table[0].findall(".//th")

col = []

for t in title:
    name = t.text_content()
    col.append(name)
print(col)

# data
content = table[0].findall(".//td")

data = []
for c in content:
    if c.text_content() != "":
        data.append(c.text_content())

a = np.array(data).reshape(-1, len(col))

df = pd.DataFrame(a, columns=col)
print(df)

