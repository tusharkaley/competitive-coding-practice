#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'closest' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#
def closest(s, queries):
    close_store = [-1]*len(s)
    alph_dict = dict()
    for i in range(0, len(s)):
        char_val = s[i]
        if char_val not in alph_dict:
            close_store[i] = -1
        else:
            temp = close_store[alph_dict[char_val]]
            close_store[i] = alph_dict[char_val]
            if temp == -1:
                close_store[alph_dict[char_val]] = i 
            else:
                close_store[alph_dict[char_val]] = check_distance(alph_dict[char_val], close_store[alph_dict[char_val]], i)
        alph_dict[s[i]]= i
    op= list()
    for query in queries:
        op.append(close_store[query])
    return op

def check_distance(prev_idx, prev_val, curr):
    dist1 =  prev_idx-prev_val
    dist2 =  curr - prev_idx
    ret_val = 0
    if dist1>dist2:
        ret_val = curr
    else:
        ret_val = prev_val
  
    return ret_val

if __name__ == '__main__':
    s = "mmhmoohwhnn"
    queries = [8, 2, 6]
    result = closest(s, queries)
    print(result)
    
