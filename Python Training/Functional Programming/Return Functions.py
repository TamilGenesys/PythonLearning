# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:04:28 2021

@author: tamil
"""


def brewTea():
    def tea():
        print(" Tea is ready ")
    return tea 


refresh = brewTea()
refresh()


input = 10

def multiplier(x):
    def multiply(num):
        print(num * x)
    return multiply

double = multiplier(2)
double(input)


triple = multiplier(3)
triple(input)