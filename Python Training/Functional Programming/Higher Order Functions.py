# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:45:41 2021

@author: tamil
"""
# Higher Order Functions help in refactoring and helps in keeping clean code, they also help in
# Argument checking for a function


def div (x, y):
    return x/y


def higherorderfunc(func):
    def argscheck(*args):
        if args[1] == 0:
            print(" Operation Terminated Div by Zero ")
            return
        else:
            return func(*args)
    
    return argscheck

higherorder_func = higherorderfunc(div)

print ( higherorder_func (2,3) )
print ( higherorder_func (2,0) )