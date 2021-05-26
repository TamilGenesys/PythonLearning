# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:25:31 2021

@author: tamil
"""


num_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list( filter( lambda x: x%2 == 0, num_list ))
print(even_list)


triple_list = list ( map ( lambda x: x*3, num_list))
print(triple_list)