# -*- coding: utf-8 -*-
"""
Created on Mon May 24 08:03:12 2021

@author: tamil
"""

#Choosing functions based on a criteria using ternery operation


def api_prod():
    print(" This is Prod Data ")


def api_dev():
    print(" This is Dev Data")
    return {
        "environment" : "Dev",
        "version" : 1.22,
        "build label": "Dev_Action_Fetch"}

ENV = "dev"

fetch_data = api_dev if ENV == "prod" else api_dev

api_data = fetch_data()
print(api_data)
print(api_data["build label"])