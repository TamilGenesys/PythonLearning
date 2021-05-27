# -*- coding: utf-8 -*-
"""
Created on Thu May 27 22:12:26 2021

@author: tamil
"""

# Partial Applications
def combine( first_name ):
    def inner( middle_name, last_name ):
        print(f" Legal Name is {first_name.title()} {middle_name.title()} {last_name.title()}")
        return
    return inner

legal_name = combine("albus")
legal_name("severes","Potter")

#currying
def currying( first_name ):
    def currying_inner( middle_name ):
        def currying_innermost(last_name):
            print(f" Legal Name is {first_name.title()} {middle_name.title()} {last_name.title()}")
            return
        return currying_innermost
    return currying_inner

legal_name_currying = currying("Thomas")
legal_name_currying_1 = legal_name_currying("marvalo")
legal_name_currying_1("riddle")

# Easy Way

currying("Facebook")("amazon")("Netflix")
