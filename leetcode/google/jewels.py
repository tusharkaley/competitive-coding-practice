class Solution:
	def numJewelsInStones(self, J, S):
		jewels_list = list(J)
		count = 0
		for st in S:
			if st in jewels_list:
				count = count + 1 
		return count

if __name__ == '__main__':
	s = Solution()
	J = "aA"
	S = "aAAbbbb"
	print(s.numJewelsInStones(J, S))