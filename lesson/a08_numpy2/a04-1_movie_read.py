'''
Created on 2017-07-26 16:58

@ product name : PyCharm Community Edition

@ author : yoda
'''

file = open("test_movie1.txt", "r", encoding="UTF-8")

lines = file.readlines()
title = []
price = []

for idx, line in enumerate(lines):
    line = line.rstrip()
    if idx%2 == 1:
        price.append(line)
    else:
        title.append(line)

print(title)
print(price)
for i in range(0, len(price)):
    print(title[i], price[i])