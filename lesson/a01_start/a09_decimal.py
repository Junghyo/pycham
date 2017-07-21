'''
Created on 2017. 7. 19.

@author: kitcoop
'''
from decimal import Decimal
hap = Decimal(0.0)
delta= Decimal('0.01')
for i in range(0,999):
    hap += delta
print("hap:", hap)