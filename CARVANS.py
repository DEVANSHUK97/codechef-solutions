# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 03:22:04 2020

@author: dkhurm
"""


t = int(input())
for _ in range(t):
    n = int(input())
    speeds = list(map(int,(str(input()).split(' '))))
    ans = 0
    max_possible = speeds[0]
    for speed in speeds:
        if speed <= max_possible:
            ans += 1
            max_possible = speed
    print(ans)  
