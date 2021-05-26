# -*- coding: utf-8 -*-
"""
Created on Wed May 26 07:50:15 2021

@author: tamil
"""

# Map Function is used for performing Transformation without having to use explicit loops. 
# Map function takes atlleast two arguments (func, iterable )
# Iterable -> Ususally a list and the func is applied to every item in the list

import math

apple = "Apple"
print( list ( apple ))

#Op : ['A', 'p', 'p', 'l', 'e']


mobile_list = ["Apple", "OnePlus", "Samsung", "Mi", "Oppo"]

mod_mobile_list = list( map( list, mobile_list))
print(mod_mobile_list)


square_list = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
sqrt_list = list( map(math.sqrt, square_list))
print(sqrt_list)


def add(x,y):
    return x+y


a_list = [ 1, 2, 3, 4, 5 ]
b_list = [ 5, 10, 15, 20, 25]

add_list = list( map(add, a_list, b_list))
print(add_list)