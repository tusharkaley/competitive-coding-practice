def spiral_matrix(matrix):
	shift = ((0,1),(1,0),(0,-1),(-1, 0))
	direction = x=y =0
	op =[]
	m = len(matrix)
	n = len(matrix[0])
	for _ in range(len(matrix)* len(matrix[0])):
		op.append(matrix[x][y])
		matrix[x][y] = 0
		next_x, next_y = x+shift[direction][0], y+shift[direction][1]
		if next_x not in range(0, m) or next_y not in range(0,n) or matrix[next_x][next_y] == 0:
			direction = (direction+1) & 3
			next_x, next_y = x+shift[direction][0], y+shift[direction][1]
		x, y = next_x, next_y
	return op

if __name__ == '__main__':
	ip = [[ 1, 2, 3 ]]
	print(spiral_matrix(ip))


