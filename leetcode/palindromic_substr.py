class Solution:
    def countSubstrings(self, s):
    	# One solution is to start at every element and go outwards counting the palindromes But this is only for odd palindromes 
    	# Other solution is for every size of strings from 2 to n find which of those are palindromes Complexity n^2
    	# 
if __name__ == '__main__':
	s = Solution()
	ip = "aaa"
	print(s.countSubstrings(ip))