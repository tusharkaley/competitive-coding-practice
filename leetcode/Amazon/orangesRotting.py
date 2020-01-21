# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid):
        stack = []
        shift = ((-1,0),(0,1),(1,0),(0,-1))
        if len(grid) == 1 and len(grid[0]) ==1:
            if grid[0][0] ==1:
                return -1
            else:
                return 0
        for i in range(len(grid)):
        	for j in range(len(grid[0])):
        		if grid[i][j] == 2:
        			stack.append((i,j))
        count = -1
        while stack:
        	temp = []
        	for q in stack:
        		i, j = q[0], q[1]
        		# check all four neighbours
        		for k in range(4):
        			ti, tj = i+shift[k][0], j+shift[k][1]
        			if ti in range(len(grid)) and tj in range(len(grid[0])) and grid[ti][tj] == 1:
        				grid[ti][tj] = 2
        				temp.append((ti,tj))
        	stack.clear()
        	stack.extend(temp)
        	temp.clear()
        	count+=1
        for i in range(len(grid)):
        	for j in range(len(grid[0])):
        		if grid[i][j] == 1:
        			return -1
        return count

if __name__ == '__main__':
	s = Solution()
	grid = [[2,1,1],[1,1,0],[0,1,1]]
	# grid = [[2,1,1],[0,1,1],[1,0,1]]
	grid = [[0,2]]
	print(s.orangesRotting(grid))