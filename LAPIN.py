# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 03:22:04 2020

@author: dkhurm
"""


t = int(input())

for _ in range(t):
    string = str(input())
    left_half = sorted(string[:len(string)//2])
    right_half = sorted(string[len(string)//2 + len(string)%2:])
    if left_half == right_half:
        print("YES")
    else:
        print("NO")
