# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:01:09 2021

@author: tamil
"""
# This is an small exercise to find the average salary of non-developers using list Comprehension

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
    
    
# Using List Comprehension to filter the non-developers

non_developers = [ emp for emp in employees if emp['job_title'] != "developer"]
print(non_developers)


# Using List Comprehension to get the Salary

non_developers_salary = [ emp['salary'] for emp in non_developers ]
print(non_developers_salary)

# Sum function to get the sum of all salries
non_developers_salary_total = sum(non_developers_salary)
print( "The Average Salary of Non_Developers is ", non_developers_salary_total/len(non_developers_salary))


