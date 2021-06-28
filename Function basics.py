# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:35:54 2021

@author: ARUNAJA GEETHAPRASAD
"""

###ARGUMENTS

def my_function(fname):
    print(fname + " Potter")
    
my_function("James")
my_function("Lily")
my_function("Harry")

###ARBITARY ARGUMENTS

def my_function(*kids):
    print("The youngest kid is "+ kids[2])
    
my_function("James Sirius","Lily Luna","Albus Severus")

#### KEY ARGUMENTS

def my_function(child1,child2,child3):
    print("The youngest kid is "+ child3)
    
my_function(child1="James Sirius",child2= "Lily Luna",child3= "Albus Severus")

##### ARBITARY KEYWORD ARGUMENTS

def my_function(**kid):
    print("His last name is "+ kid["lname"])
    
my_function(fname ="Harry", lname = " Potter" )


#### DEFAULT PARAMETER VALUE

def my_function(country = "Norway"):
    print("My country is "+ country)
    
my_function("India")
my_function()
my_function("Sweden")

### PASSING A LIST AS AN ARGUMENT

fruits = ["apple","orange","banana"]
def my_function(foods):
    for x in foods:
        print (x)
my_function(fruits)

### RETURINING A FUNCTION

def my_function(x):
    return 5*x

print(my_function(10))

#### THE PASS STATEMENT

def my_function():
        pass
my_function()


