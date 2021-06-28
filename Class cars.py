# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 23:49:15 2021

@author: ARUNAJA GEETHAPRASAD
"""

##CLASS

class Cars:
    def __init__(self,doors,wheels):
        self.doors=doors
        self.wheels=wheels
        print("This  is a normal car with " + self.doors + " doors" + " and " + self.wheels + " wheels")
    
    def purpose1(self):
        print("Normal Car")
##INHERITANCE

class Sportscar(Cars):
    def __init__(self,doors,wheels,engine):
        Cars.__init__(self,doors,wheels)
        self.engine=engine
        print("This  is a Sports car with " + self.doors + " doors" + " and " + self.wheels + " wheels and " + self.engine + " Engines")
        
    def purpose2(self):
        print("Sports Car")
    
a= input("Enter no of doors:")
b= input("Enter no of wheels:")

##OBJECTS

c1 =Cars(a,b)
c1.purpose1()

x= input("Enter no of doors:")
y= input("Enter no of wheels:")
z= input("Enter no of engines:")

c2=Sportscar(x,y,z)
c2.purpose2()