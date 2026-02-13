# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 15:17:52 2026

@author: User
"""

n = int(input("Enter number: ")) 
fact = 1
for i in range(1, n + 1): 
 fact = fact*i
print("Factorial:", fact)