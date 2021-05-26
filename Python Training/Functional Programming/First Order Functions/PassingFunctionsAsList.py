# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:11:04 2021

@author: tamil
"""

import math

def twice(x):
    return 2*x


def triple(x):
    return 3*x


def incr(x):
    return x+1


def decr(x):
    return x-1

funcList = [
    twice,
    triple,
    incr,
    decr,
    math.sqrt]

num = 4
for func in funcList:
    num = func(num)
    
    
    
print(num)