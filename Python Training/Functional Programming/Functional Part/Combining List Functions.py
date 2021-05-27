# -*- coding: utf-8 -*-
"""
Created on Thu May 27 08:47:29 2021

@author: tamil
"""
# This is an small exercise to find the average salary of non-developers using
# Map, Reduce and Filter

from functools import reduce
employees = [{
    'name': 'Jane',
    'salary': 90000,
    'job_title': 'developer'
}, {
    'name': 'Bill',
    'salary': 50000,
    'job_title': 'writer'
}, {
    'name': 'Kathy',
    'salary': 120000,
    'job_title': 'executive'
}, {
    'name': 'Anna',
    'salary': 100000,
    'job_title': 'developer'
}, {
    'name': 'Dennis',
    'salary': 95000,
    'job_title': 'developer'
}, {
    'name': 'Albert',
    'salary': 70000,
    'job_title': 'marketing specialist'
}]
    
    
#filter the non-dveleopers    
    
def is_non_dev ( emp ):
    return emp['job_title'] != "developer"

non_developers = list( filter( is_non_dev, employees ))
print( non_developers )



# Use Map to get the Salary of the Non-Developers

def get_salary( emp ):
    return emp['salary']

non_developers_salary = list( map ( get_salary, non_developers ))
print(non_developers_salary)


# Use Reduce to get the Total Salary of Non-Developers

def get_salary_total( init, sal ):
    return init+sal

non_developers_salary_total = reduce(get_salary_total,non_developers_salary )
print(" The Average Non-Developer Salary is ",non_developers_salary_total/len(non_developers_salary))














