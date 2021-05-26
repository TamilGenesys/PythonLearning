# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:06:26 2021

@author: tamil
"""

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

a = 70
b = 80

def funcAsArguments(func):
    return func(a,b)


print( funcAsArguments(add) )
print( funcAsArguments(sub) )

def strFunc(func):
    return func("Harry", "Potter")


def legalFormat(first_name, last_name):
    print ( f'{last_name}, {first_name}' )


strFunc(legalFormat)