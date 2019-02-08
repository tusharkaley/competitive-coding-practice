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
    op = list()
    close_store= dict()
    temp = 0
    val = -1
    # Looping over all queries
    for query in queries:
        # k is the element to the right of the 'query'
        # i is the element to the left of the 'query'
        k= query+1
        i = query-1
        # print("query: {}".format(query))
        # if we have already stored query in close_store that means we know that "query" is close to some other element we've seen before
        if query in close_store:
            val = close_store[query]
            # val stores the element to which query is the closest. 
            # Now we just check if anyone else is closer to 'query' than val

            if val>query:
                # this means we just check to the right of query since we know closest in the left direction is val
                # print("first if")
                # setting k to length ensures movement only in one direction
                k = len(s)
                temp = helper(query, s, k, i, val)
            elif val < query:
                # this means we just check to the left of query since we know closest in the right direction is val
                # print("second if")
                # setting i to -1 ensures movement only in one direction
                i = -1
                temp = helper(query, s, k, i, val)        
            else:
                temp = val
        else:
            # case where we've not encountered this element before
            temp = helper(query, s, k, i, val)    
        if temp!= -1:
            # store in dict only if helper returns a valid value
            close_store[temp] = query
        if temp in close_store:
            # Conflict so poping the value out
            close_store.pop(temp)
    
        op.append(temp)
    return op

def helper(q, s, k , i, val):
    # Write your code here
        if q >=len(s):
            return -1
        length = abs(val-q)
        count = 1
        target_val = s[q]
        # print("target_val {}, length {}, i {}, k {}".format(target_val, length, i, k))
        while (i>=0 or k<len(s)):
            if val!= -1:
                # we go past the length of the current best the just return the current best
                if count == length+1:
                    return val
                if i>=0:
                    if s[i] == target_val:
                        if count == length:
                            return min(i,val)
                        else:    
                            return i
                if k<len(s):
                    if s[k] == target_val:
                        if count == length:
                            return min(k,val)
                        else:
                            return k
                count = count + 1
            else:    
                # just go one element at a time in both directions till you find a match
                if i>=0:
                    if s[i] == target_val:
                        return i
                if k<len(s):
                    if s[k] == target_val:
                        return k
            k = k+1
            i = i-1
        if val!= -1:
            return val   
        else:
            return -1


if __name__ == '__main__':
    s = "mmhmoohwhnn"
    queries = [8, 2, 6]
    result = closest(s, queries)
    print(result)
    
