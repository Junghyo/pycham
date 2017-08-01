'''
Created on 2017-08-01 14:53

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.image as mpimg
# matplotlib.image의 imread("이미지경로")
img = mpimg.imread("wordscloud.jpg")
plt.imshow(img)
plt.show()