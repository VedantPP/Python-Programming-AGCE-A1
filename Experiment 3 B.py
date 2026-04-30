# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:13:31 2026

@author: Vedant Banugade
"""
def simple_interest(principal, rate, time):
  si = (principal * rate * time) / 100
  return si
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))
interest = simple_interest(p, r, t)
print("Simple Interest is:", interest)
