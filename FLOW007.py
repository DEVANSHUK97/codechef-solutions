# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 03:22:04 2020

@author: dkhurm
"""


t = int(input())

for _ in range(t):
    number = str(input())
    print(int(number[::-1]))