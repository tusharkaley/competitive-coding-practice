class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        try:
        	output = list()
        	for row in A:
        		new_row = list()
        		for i in range(len(row)-1, -1, -1):
        			if row[i] == 0:
        				new_row.append(1)
        			else:
        				new_row.append(0)
        		output.append(new_row)
        	return output
        	
        except Exception as e:
        	raise e
if __name__ == '__main__':
	s = Solution()
	inp = [[1,1,0],[1,0,1],[0,0,0]]
	print(s.flipAndInvertImage(inp))