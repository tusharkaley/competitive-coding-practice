class Solution(object):
	def numIslands(self, grid):
		reg = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == "1":
					grid = self.paint_region(grid, i, j)
					reg=reg + 1		
		return reg	

	def paint_region(self, matrix, r,c):
		matrix[r][c] = "2"
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
		if left == "1":
			matrix = self.paint_region(matrix, r, c-1)
		if right == "1":
			matrix = self.paint_region(matrix, r, c+1)
		if bottom == "1":
			matrix = self.paint_region(matrix, r+1, c)
		if top == "1":
			matrix = self.paint_region(matrix, r-1, c)
		return matrix

if __name__ == '__main__':
	s = Solution()
	ip = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
	print(s.numIslands(ip))

	