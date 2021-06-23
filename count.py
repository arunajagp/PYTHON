# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 00:07:52 2021

@author: ARUNAJA GEETHAPRASAD
"""
def most_frequent():
    count={}
    for i in str:
        if i in count.keys():
            count[i]+=1
        else:
            count[i]=1
    print(count)
        
str=input("Please enter a string:")
print("The string is:",str)

most_frequent()

