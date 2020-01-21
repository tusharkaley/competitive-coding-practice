import time
class Solution:
	def wordBreak(self, s, wordDict):
		grid = [[None]*len(s) for i in range(len(s))]
		word_dict = dict()
		for word in wordDict:
			word_dict[word] = True
		i = 0
		j = 0
		incr = 1
		seed = 0
		while j < len(s):
			while i< len(s) and j < len(s):
				grid[i][j] = self.checkGrid(grid, s, i, j+1, word_dict)
				i += incr
				j += incr
			seed +=1
			i = 0
			j = seed
		# for i in range(len(s)):
		# 	for j in range(len(s)):
		# 		print "{} \t".format(grid[i][j]),
		# 	print("")
		return grid[0][len(s)-1]
			

	def checkGrid(self, grid, s, i, j, wordDict):
		# print("i: j: {}: {}".format(i,j))
		if i==j:
			if s[i:j] in wordDict:
				return True
			else:
				return False
		else:

			if s[i:j] in wordDict:
				return True
			else:
				for ind in range(i+1, j):
					val1 = self.check_single_value(s, i, ind, grid, wordDict)
					val2 = self.check_single_value(s, ind, j, grid, wordDict)
					# print("Val1: Val2: {}: {}".format(val1, val2))
					if val1 and val2:
						return True
		return False

	def check_single_value(self, chk_str, i, j, grid, wordDict):
		# print("checking for: i: j: {}: {}: {} : {}".format(i,j,chk_str, chk_str[i:j]))
		if grid[i][j-1] != None and grid[i][j-1]:
			return True
		else:
			grid[i][j-1] = chk_str[i:j] in wordDict
			return grid[i][j-1]


if __name__ == '__main__':
	s = Solution()
	st = "leetcode"
	wordDict = ["leet", "code"]
	st = "applepenapple"
	wordDict = ["apple", "pen"]
	st = "catsandog"
	wordDict = ["cats", "dog", "sand", "and", "cat"]
	st = "bb"
	wordDict = ["a","b","bbb","bbbb"]
	st = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
	wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
	start = time.time()
	print(s.wordBreak(st, wordDict))
	end = time.time()
	print(end-start)
		