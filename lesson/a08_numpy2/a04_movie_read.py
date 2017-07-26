'''
Created on 2017-07-26 16:19

@ product name : PyCharm Community Edition

@ author : yoda
'''

f = open("test_movie.txt", "r", encoding="UTF-8")

txt = f.read()

txt_l = txt.split("\n")
a = txt.rstrip()
i = 0
while i < len(txt_l):
    if txt_l[i] == "":
        del[txt_l[i]]
    i += 1

del[txt_l[0]]
print(txt_l)


import numpy as np

t = []
p = []
i = 0
while i < len(txt_l):
    if i % 2 == 0:
        t.append(txt_l[i])
    else:
        p.append(txt_l[i])
    i += 1
print(t)
print(p)

c = np.c_[t, p]

print(c)
print(c.ndim)
print(c.shape)
print(type(c))
d = np.array(["제목", "관람료"])
e = np.vstack([d, c])
f2 = open("test_movie2.txt", "w", encoding="UTF-8")
f2.write(str(e))
f2.close()
