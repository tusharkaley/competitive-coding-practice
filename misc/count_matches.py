#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countMatches' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid1
#  2. STRING_ARRAY grid2
#
def countMatches(grid1, grid2):
    matches= list()
    matches = [[0]*len(grid1) for _ in range(len(grid1))]
    for i in range(0,len(grid1)):
        for j in range(0,len(grid1)):
            temp1 = grid1[i][j]
            temp2 = grid2[i][j]
            if temp2 == temp1:
                if temp2=='1':
                    matches[i][j] = 1
    region = 0
    for i in range(0,len(grid1)):
        for j in range(0,len(grid1)):
            if checkNeighbours(i,j,(matches))==2:
                matches[i][j] = -1
                region= region + 1
            elif checkNeighbours(i,j,(matches))==1:
                matches[i][j] = -1
            else:
                continue
    return region

def check_neighbours(r, c, mat):
    left = -10
    right = -10
    top = -10
    bottom = -10

    if matches[r][c] == 0:
        incr = 0
    elif matches[r][c] == -1:
        incr = 0
    else
        try:
            left = mat[r][c-1]
        except Exception as e:
            pass
        try:
            right = mat[r][c+1]
        except Exception as e:
            pass
        try:
            top = mat[r-1][c]
        except Exception as e:
            pass
        try:
            bottom = mat[r+1][c]
        except Exception as e:
            pass
        
        if left==-1:
            incr = 1
        elif left ==1:
            mat[r][c-1] = -1

         if right==-1:
            incr = 1
        elif right ==1:
            mat[r][c+1] = -1

         if top==-1:
            incr = 1
        elif top ==1:
            mat[r-1][c] = -1

         if bottom==-1:
            incr = 1
        elif bottom ==1:
            mat[r+1][c] = -1




def checkNeighbours(r,c, matches):
    n = len(matches)
    incr =2
    if matches[r][c] == 0:
        incr = 0
    elif matches[r][c] == -1:
        incr = 0
    else:
        if r==0:
            if c == 0:
                # Check r+1 and c+1
                if matches[r+1][c]==-1:
                    incr = 1
                elif matches[r+1][c] == 1:
                    matches[r+1][c]=-1
                    incr = 1

                if matches[r][c+1]==-1:
                    incr = 1
                elif matches[r][c+1]==1:
                    matches[r][c+1] = -1
                    incr = 1

            elif c == n-1:
                if matches[r+1][c]==-1: 
                    incr = 1
                elif matches[r+1][c]==1:
                    matches[r+1][c]=-1
                    incr = 1

                if matches[r][c-1]==-1:
                    incr = 1
                elif matches[r][c-1]==1:
                    matches[r][c-1]=-1
                    incr=1
            else:
                if matches[r+1][c]==-1:
                    incr = 1
                elif matches[r+1][c]==1:
                    incr=1
                    matches[r+1][c] =-1
                if matches[r][c-1]==-1:
                    incr=1
                elif matches[r][c-1]==1:
                    incr=1
                    matches[r][c-1]=-1

                if matches[r][c+1]==-1:
                    incr = 1
                elif matches[r][c+1]==1:
                    matches[r][c+1]=-1
                    incr = 1
        elif r>0 and r < n-1:
            if c == 0:
                if matches[r+1][c]==-1:
                    incr = 1
                elif matches[r+1][c]==1: 
                    incr = 1
                    matches[r+1][c]= -1
                if matches[r][c+1]==-1:
                    incr = 1
                elif matches[r][c+1]==1:
                    incr = 1
                    matches[r][c+1]==-1

                if matches[r-1][c]==-1:
                    incr = 1
                elif matches[r-1][c]==1: 
                    matches[r][c+1]==-1
                    incr = 1

            elif c == n-1:
                if matches[r+1][c]==-1:
                    incr = 1
                elif matches[r+1][c]==1:
                    matches[r+1][c]=-1
                    incr = 1
                if matches[r][c-1]==-1:
                    incr = 1
                elif matches[r][c-1]==1:
                    matches[r][c-1]=-1
                    incr = 1
                if matches[r-1][c]==-1:
                    incr =1
                elif matches[r-1][c]==1:
                    matches[r-1][c]= -1
                    incr = 1
            else:
                if matches[r+1][c]==-1:
                    incr = 1
                elif matches[r+1][c]==1:
                    matches[r+1][c]=-1
                    incr = 1
                
                if matches[r][c-1]==-1:
                    incr = 1
                elif matches[r][c-1]==1:
                    matches[r][c-1]=-1
                    incr = 1
                
                if matches[r][c+1]==-1:
                    incr = 1
                elif matches[r][c+1]==1:
                    matches[r][c+1]=-1
                    incr = 1
                
                if matches[r-1][c]==-1:
                    incr = 1
                elif matches[r-1][c]==1:
                    matches[r-1][c]=-1
                    incr = 1
        else:
            if c == 0:
                if matches[r-1][c]==-1:
                    incr = 1
                elif matches[r-1][c]==1:
                    matches[r-1][c]=-1
                    incr = 1                    
                if matches[r][c-1]==-1:
                    incr = 1
                elif matches[r][c-1]==1:
                    matches[r][c-1]=-1
                    incr = 1
            elif c == n-1:
                if matches[r-1][c]==-1:
                    incr = 1 
                elif matches[r-1][c]==1:
                    matches[r-1][c]=-1
                    incr = 1
                
                if matches[r][c-1]==-1:
                    incr = 1
                elif matches[r][c-1]==1:
                    matches[r][c-1]=-1
                    incr = 1
            else:
                if matches[r-1][c]==-1:
                    incr = 1
                elif matches[r-1][c]==1:
                    matches[r-1][c]=-1
                    incr = 1
                if matches[r][c-1]==-1:
                    incr = 1
                elif matches[r][c-1]==1:
                    matches[r][c-1]=-1 
                    incr = 1
                if matches[r][c+1]==-1:
                    incr = 1
                elif matches[r][c+1]==1:
                    matches[r][c+1]=-1
                    incr = 1
    return incr
		
if __name__ == '__main__':

	grid1 = ['001', '011', '100']
	grid2 = ['001', '011', '101']

	result = countMatches(grid1, grid2)
	print(result)

	
