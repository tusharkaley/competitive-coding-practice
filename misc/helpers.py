def check_neighbours(r, c, mat):
	left = -10
	right = -10
	top = -10
	bottom =-10

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
	if left:
		print("left: {}".format(left))
	if right:
		print("right: {}".format(right))
	if top:
		print("top: {}".format(top))
	if bottom:
		print("bottom: {}".format(bottom))


if __name__ == '__main__':
	matches = [[0]*4 for _ in range(4)]
	matches[0][1] = 6
	matches[1][0] = 8

	check_neighbours(0,0, matches)