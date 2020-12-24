# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 03:22:04 2020

@author: dkhurm
"""

def log(number, base):
    exponent = 0
    value = base
    while number%value == 0:
        exponent += 1
        value *= base
    return exponent 
        
t = int(input())
for _ in range(t):
    n = int(input())
    power_of_2 = 0
    power_of_5 = 0
    for i in range(1, n+1):
        power_of_2 += log(i,2)
        power_of_5 += log(i,5)
    print(min(power_of_2, power_of_5))  
