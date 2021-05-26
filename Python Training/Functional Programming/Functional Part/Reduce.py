# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:37:14 2021

@author: tamil
"""

# Reduce function will reduce the giver iterable to a single item

import math
from functools import reduce

num_list = [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]

def sqrt_sum( acc, num ):
    return acc + math.sqrt(num)


sqrt_total = reduce(sqrt_sum, num_list, 0)
print(sqrt_total)


name_list = [ "SS Hyderabad", "Anjappar", "Thalappakatti", "Star", "Paradise", "Sukkubhai"]

def unite(acc, name):
    return acc + " "+name

shops = reduce(unite, name_list)
print(shops)
