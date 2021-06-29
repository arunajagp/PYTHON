# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:17:05 2021

@author: ARUNAJA GEETHAPRASAD
"""

##TASK NO :1

## TO COMPUTE THE AREA OF A CIRCLE

r = float(input("The radius of the circle is:"))
a = 3.14*r*r
print("The area of the circle is:",a)

##TASK NO:2

## TO FIND THE EXTENSTION OF A GIVEN FILE

file_name = input("Input the file name:")
file_extn = file_name.split(".")
print("The extension of the file is :",file_extn[1])



file_name = input("Input the file name:")
file_extn = file_name.split(".")
file_extns = file_extn[1]
if file_extns== "py":
  print("The extension of the file is :'python'")
else:
  print("None")
  
  file_extns = file_extn[1]