'''
Created on 2017-08-02 19:02

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.image as mpimg
img = mpimg.imread("../a13_pytagcloud/wordscloud.jpg")
## pyplot.imshow(이미지객체)
imgplot = plt.imshow(img)
plt.show()
