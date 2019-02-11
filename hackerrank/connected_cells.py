import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def connectedCell(matrix):

	reg = 0
	maxx = 0
	count =0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				matrix, temp = paint_cells(matrix, i, j, count)
				if temp > maxx:
					maxx = temp
				# print("i: {}, j: {}".format(i,j))
                print(temp)
                print(matrix)

	return maxx
def paint_cells(matrix, i, j, count):
	print("i: {}, j: {}".format(i,j))
	if matrix[i][j]==2:
		return matrix, count
	count = count+1
	matrix[i][j] = 2
	left = -10
	right = -10
	top = -10
	bottom = -10
	top_left = -10
	top_right = -10
	bottom_left = -10
	bottom_right = -10

	try:
		if j-1>=0:
			left = matrix[i][j-1]
	except Exception as e:
		pass
	try:

		right = matrix [i][j+1]
	except Exception as e:
		pass
	try:
		if i-1>=0:
			top = matrix[i-1][j]
	except Exception as e:
		pass
	try:
		bottom = matrix[i+1][j]
	except Exception as e:
		pass
	try:
		if j-1>=0 and i-1>=0:
			top_left = matrix[i-1][j-1]
	except Exception as e:
		pass
	try:
		if i-1>=0:
			top_right = matrix [i-1][j+1]
	except Exception as e:
		pass
	try:
		if j-1>=0:
			bottom_left = matrix[i+1][j-1]
	except Exception as e:
		pass
	try:
		bottom_right = matrix[i+1][j+1]
	except Exception as e:
		pass


	if left==1:
		matrix, count = paint_cells(matrix, i, j-1, count)
	if right==1:
		matrix, count = paint_cells(matrix, i, j+1, count)
	if top==1:
		matrix, count = paint_cells(matrix, i-1, j, count)
	if bottom==1:
		matrix, count = paint_cells(matrix, i+1, j, count)
	if top_left==1 and top != 1 and left!= 1 and top != 2 and left!= 2:
		print("top_left")
		matrix, count = paint_cells(matrix, i-1, j-1, count)
	if bottom_right==1 and right!=1 and bottom!=1 and right!=2 and bottom!=2:
		print("bottom_right")
		matrix, count = paint_cells(matrix, i+1, j+1, count)
	if top_right==1 and right!=1 and top!=1 and right!=2 and top!=2:
		print("top_right")
		matrix, count = paint_cells(matrix, i-1, j+1, count)
	if bottom_left==1 and bottom != 1 and left !=1 and bottom != 2 and left !=2:
		
		# print("bottom_left")
		matrix, count = paint_cells(matrix, i+1, j-1, count)
	return matrix, count

if __name__ == '__main__':
	ip = [[0,1,1,1,1],[1,0,0,0,1],[1,1,0,1,0], [0,1,0,1,1],[0,1,1,1,0]]
	# ip = [[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0]]
	print(connectedCell(ip))

