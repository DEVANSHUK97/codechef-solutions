# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 21:08:40 2020

@author: dkhurm
"""

t = int(input())
for _ in range(t):
    n_o = str(input()).split(' ')
    n = n_o[0]
    o = n_o[1]
    limit = {'INDIAN':200, 'NON_INDIAN':400}
    total = 0
    for _ in range(n):
        action = str(input()).split(' ')
        if action[0] == 'CONTEST_WON':
            total += (300 + max(20-action[1], 0))
        elif action[0] == 'TOP_CONTRIBUTOR':
            total += 300
        elif action[0] == 'BUG_FOUND':
            total += action[1]
        elif action[0] == 'CONTEST_HOSTED':
            total += 50
        else:
            print('wtf!')
    print(total//limit[o])