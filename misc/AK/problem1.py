
import math
def find_minima(n, m):
    op = list()
    for i in range(n):
    	for j in range(n):
    		if check_neighbors(m, i, j):
    			op.append(m[i][j])
    op.sort()
    return op[:4]

def check_neighbors(matrix, i, j):
	
	left = float("inf")
	right = float("inf")
	top = float("inf")
	bottom = float("inf")
	top_left = float("inf")
	top_right = float("inf")
	bottom_left = float("inf")
	bottom_right = float("inf")
	num = matrix[i][j]
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

	if not math.isinf(left):
		if left <= num:
			return False

	if not math.isinf(right):
		if right < num:
			return False

	if not math.isinf(top)::
		if top < num:
			return False
	
	if not math.isinf(bottom)::
		if bottom < num:
			return False
	
	if not math.isinf(bottom_right)::
		if bottom_right < num:
			return False
	
	if not math.isinf(bottom_left)::
		if bottom_left < num:
			return False
	
	if not math.isinf(top_left)::
		if top_left < num:
			return False
	
	if not math.isinf(top_right)::
		if top_right < num:
			return False
	
	return True

if __name__ == '__main__':

	grid1 = ['0100', '1001', '0011', '0011']
	grid2 = ['0101', '1001', '0011', '0011']

	result = countMatches(grid1, grid2)
	print(result)
