class Solution:
	def validPalindrome(self, s: str) -> bool:
		num_deletions = 0
		i = 0
		j = len(s)-1
		while i<j:
			if s[i]==s[j]:
				i+=1
				j-=1
				continue
			else:
				if s[i+1] == s[j]:
					num_deletions ++
					if num_deletions>1:
						return False
		return True

if __name__ = "__main__":
	s = Solution()
	st = "aba"
	print(s.validPalindrome(st))


