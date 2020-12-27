# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:27:37 2020

@author: dkhurm
"""

t = int(input())
for _ in range(t):
    g = int(input())
    for _ in range(g):
        i_n_q = str(input()).split(' ')
        i = int(i_n_q[0])
        n = int(i_n_q[1])
        q = int(i_n_q[2])
        final_count_initial_face = n//2 
        final_count_other_face = final_count_initial_face + n%2
        if q == i:
            print(final_count_initial_face)
        else:
            print(final_count_other_face)
    