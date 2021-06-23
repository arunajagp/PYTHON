# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 23:18:54 2021

@author: ARUNAJA GEETHAPRASAD
"""

def my_function():
    print("This is the function")
    
print("Before the function")

my_function()

###################################################

##DEFAULT FUNCTION
def my_fun(name):
    print("Hello ",name)
print("Before function")
my_fun("Harry")

def my_fun(name="Hermione"):
    print("Hello ",name)
print("Before function")
my_fun()

def my_fun(name="Hermione"):
    print("Hello ",name)
print("Before function")
my_fun("Sirius")

##RETURNING FUNCTION

def my_function(num):
    return 5*num
output =my_function(10)
print(output)

################################################################

###BUIT-IN FUNCTIONS

import random
ouput = random.randint(1,6)
print(output)

a="i am Arunaja"
print(a.split(" "))
print(a[1:9])
print(a.upper())
print(a.lower())