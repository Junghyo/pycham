'''
Created on 2017-07-27 12:05

@ product name : PyCharm Community Edition

@ author : yoda
'''

import numpy as np

a = np.arange(30)
np.savetxt("z04_test.csv", a)

b = np.loadtxt("z04_test.csv", delimiter="\t")
print(b)