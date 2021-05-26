# -*- coding: utf-8 -*-
"""
Created on Wed May 26 08:44:37 2021

@author: tamil
"""
# Filter is same as Map, however the func should return a boolean that will be used to filter the iterable

number_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(x):
    return x % 2 == 0

even_list = list ( filter( is_even, number_list ))
print(even_list)

initials = "A"

name_list = ["Anand","arun","asin","Bava","Harry","Anu","Azma","Carol","Carla"]

def checkinitial(s):
    return s[0].upper() == initials

select_list = list ( filter (checkinitial, name_list))
print(select_list)
