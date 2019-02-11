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
	# matches= list()
	matches =[[0]*len(grid1) for _ in range(len(grid1))]
	for i in range(0,len(grid1)):
		for j in range(0,len(grid1)):
			temp1 = grid1[i][j]
			temp2 = grid2[i][j]
			if temp2 == temp1:
				if temp2=='1':
					matches[i][j] = "1"
				if temp2=='0':
					matches[i][j] = "0"
			else:
				matches[i][j] = "2"
	region = 0
	for i in range(len(grid1)):
		for j in range(len(grid1[0])):
			if matches[i][j] == "1":
				matches, two_found = paint_region(matches, i, j, False)
				if not two_found:
					region=region + 1  
			if matches[i][j] == "2":
				matches, two_found = paint_region(matches, i, j, False)
	return region  

def paint_region(matrix, r,c, two_found):
	matrix[r][c] = "-1"
	left = -10
	right = -10
	top = -10
	bottom = -10
	try:
		if c-1 >= 0:
			left = matrix[r][c-1]
	except Exception as e:
		pass
	try:
		right = matrix[r][c+1]
	except Exception as e:
		pass
	try:
		if r-1>=0:
			top = matrix[r-1][c]
	except Exception as e:
		pass
	try:
		bottom = matrix[r+1][c]
	except Exception as e:
		pass
	if left == "2" or right == "2" or top== "2" or bottom=="2": 
		two_found = True
	if left == "1" or left == "2":
		matrix, two_found = paint_region(matrix, r, c-1, two_found)

	if right == "1" or right == "2":
		matrix, two_found = paint_region(matrix, r, c+1, two_found)
	if bottom == "1" or bottom=="2":
		matrix, two_found = paint_region(matrix, r+1, c, two_found)
	if top == "1" or top == "2":
		matrix, two_found = paint_region(matrix, r-1, c, two_found)
	return matrix, two_found
	
if __name__ == '__main__':

	grid1 = ['0100', '1001', '0011', '0011']
	grid2 = ['0101', '1001', '0011', '0011']

	result = countMatches(grid1, grid2)
	print(result)

	
