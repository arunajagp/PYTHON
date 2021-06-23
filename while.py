# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 14:42:19 2021

@author: ARUNAJA GEETHAPRASAD
"""


n = 15
i=1
while(i<16):
  if i % 3==0 and i%5==0:
        print("FizzBuzz")
  elif i%3==0 and i%5!=0:
        print("Fizz")
  elif i%5==0 and i%3!=0:
        print("Buzz")
  elif i%3!=0 and i%5!=0:
        print(i)
  i=i+1
