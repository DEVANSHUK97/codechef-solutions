# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:45:49 2020

@author: dkhurm
"""

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for _ in range(n):
        s_p_v = str(input()).split(' ')
        s = int(s_p_v[0])
        p = int(s_p_v[1])
        v = int(s_p_v[2])
        if v*(p//(s+1)) > ans:
            ans = v*(p//(s+1))
    print(ans)