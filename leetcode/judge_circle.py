class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        try:
        	x, y = 0, 0
        	for move in moves:
        		if move == "L":
        			x = x - 1
        		elif move == "U":
        			y = y + 1 
        		elif move == "R":
        			x = x + 1 
        		elif move == "D":
        			y = y - 1
        	if x == 0 and y == 0:
        		return True
        	else:
        		return False

        except Exception as e:
        	raise e
if __name__ == "__main__":
    s = Solution()
    nums = "UDU"
    print(s.judgeCircle(nums))
