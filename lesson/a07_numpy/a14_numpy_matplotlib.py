'''
Created on 2017-07-26 12:02

@ product name : PyCharm Community Edition

@ author : yoda
'''

import matplotlib.pylab as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.1)
print(x)
y = np.sin(x)

plt.plot(x, y)
plt.show()