# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:58:58 2020

@author: dkhurm
"""

t = int(input())

for _ in range(t):
    k_d0_d1  = list(map(int, str(input()).split(' ')))
    k = k_d0_d1[0]
    d0 = k_d0_d1[1]
    d1 = k_d0_d1[2]
    
    if k==2:
        number = 10*d0 + d1
        if number%3 == 0:
            print("YES")
        else:
            print("NO")
        continue
    
    patterns = set()
    number = [(d0), (d1), ((d0+d1)%10)]
    last3 = tuple(i for i in number[-3:])
    idx = 3
    while last3 not in patterns:
        if idx == k:
            break
        patterns.add(last3)
        number.append(sum(number)%10)
        idx += 1
        last3 = tuple(i for i in number[-3:])
    if idx == k:
        if int(''.join(map(str,number)))%3 == 0:
            print("YES")
        else:
            print("NO")
        continue
    

    number_so_far = (''.join(map(str,number)))
    pattern = ''.join([str(i) for i in last3])
    repeating_first_idx = number_so_far.index(pattern)
    repeating_second_idx = repeating_first_idx + 1 + number_so_far[repeating_first_idx+1:].index(pattern) 
    
    
    first_few = number_so_far[:repeating_first_idx]
    first_sum = (sum(map(int,list(first_few))))%3
    
    complete_pattern = number_so_far[repeating_first_idx:repeating_second_idx]
    pattern_sum = sum(map(int,list(complete_pattern)))
    pattern_len = len(complete_pattern)
    middle_sum = (pattern_sum%3*((k-repeating_first_idx)//pattern_len)%3)%3
    last_few = (k - repeating_first_idx)%pattern_len
    if last_few == 0:
        last_sum = 0
    else:
        last_sum = sum(list(map(int,complete_pattern[:last_few])))%3
    final_sum = (first_sum+middle_sum+last_sum)%3
    if final_sum == 0:
        print("YES")
    else:
        print("NO")