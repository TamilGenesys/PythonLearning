# -*- coding: utf-8 -*-
"""
Created on Wed May 26 18:51:58 2021

@author: tamil
"""
# List Comprehensions allows us to bring the behviour of map and filter fuctions

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Same as Map
double = [ x*2 for x in num_list ]
print(double)

# same as filter
even = [ x for x in num_list if x%2 == 0]
print(even)

# combine map and filter

double_even = [ x*2 for x in num_list if x%2 == 0]
print(double_even)


name_list = ["Pongal", "Vadai", "Idly", "Dosai", "Poori", "Chutney", "Sambhar", "Vadcurry", "Upma"]

# Same as Map
cap_name = [ x.upper() for x in name_list]
print(cap_name)


# Same as filter
initials = "P"
initials_name = [ x for x in name_list if x[0].upper() == initials]
print(initials_name)

# map and filter

initials_cap_name = [ x.upper() for x in name_list if x[0].upper() == initials]
print(initials_cap_name)