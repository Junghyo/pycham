'''
Created on 2017-07-24 18:24

@ product name : PyCharm Community Edition

@ author : yoda
'''

import os


def filelen(filename):
    f = open(filename, "r")
    f.seek(0, os.SEEK_END)
    return f.tell()


def countinfile(filename, char_to_find):
    count = 0
    f = open(filename, "r")
    for word in f:
        for char in word:
            if char == char_to_find:
                count += 1
    return count