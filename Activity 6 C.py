# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:35:31 2026

@author: Vedant Banugade
"""

try:
    with open("complaints.txt", "r") as file:
        print("List of Complaints:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Complaint file not found.")