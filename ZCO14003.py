# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 03:22:04 2020

@author: dkhurm
"""


t = int(input())
budgets = []
for _ in range(t):
    budgets.append(int(input()))
    
budgets = sorted(budgets)
how_many_can_afford = list(range(1,t+1))[::-1]
revenue = [budgets[i]*how_many_can_afford[i] for i in range(t)]
ans = max(revenue)
print(ans)