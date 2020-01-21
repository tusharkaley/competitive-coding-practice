from collections import Counter, defaultdict
# class Solution:
	# def findAnagrams(self, s, p):
	# 	len_p = len(p)
	# 	op = list()
	# 	for i in range(len(s)-len_p+1):
	# 		if self.check_Anagram(s[i:i+len_p], p):
	# 			op.append(i)
	# 	return op

	# def check_Anagram(self, s, p):
	# 	val = 0
	# 	count_dict = dict()
	# 	if s == p:
	# 		return True
	# 	for i in p:
	# 		count_dict[i]= count_dict.get(i,0) + 1

	# 	for j in s:
	# 		if j in count_dict:
	# 			count_dict[j]-=1
	# 	for val in count_dict.values():
 # 		 	if val != 0:
 # 		 		return False
	# 	return True
class Solution:
	def findAnagrams(self, s, p):
		i, j = 0, 0
		len_p = len(p)
		count = Counter(p)
		curr_count = defaultdict(int)
		op = list()
		fin_else = False
		while j< len(s):
			print("{}:{}".format(i,j))

			if j-i< len_p:
				print("if")
				if s[j] not in count:
					j=j+1
					i = j
					curr_count.clear()
					fin_else = False
					continue

				if s[j] in count and curr_count[s[j]]<count[s[j]]:
					print("2nd if")
					curr_count[s[j]] += 1
					j+=1
					if j>=len(s):
						if j-i == len(p):
							op.append(i)
				else:
					i = j
					fin_else = False
					curr_count.clear()
					
			else:
				print("else")
				op.append(i)
				if s[j] not in count:
					i=j+1
				elif s[i] != s[j]:
					i=j+1
					j = i
				else:
					i = i+1
					j = j+1
					fin_else = True
				curr_count.clear()
		if fin_else:
			op.append(i)
		return op


if __name__ == '__main__':
	# import sys
	# print(sys.version)
	sol = Solution()
	s = "cbaebabacd"
	p = "abc"

	# s = "baa"
	# p = "aa"
	# s = "abab"
	# p = "ab"
	s = "abacbabc"
	p = "abc"

	
	print(sol.findAnagrams(s, p))