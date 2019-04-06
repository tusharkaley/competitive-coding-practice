import math
import random

class Solution(object):
	def customSortString(self, S, T):
		"""
		:type S: str
		:type T: str
		:rtype: str
		"""
		op = ""
		t_ind = list()
		t_dict = dict()
		count = dict()
		temp = len(S)
		for t in T:
			if t in count:
				count[t] = count[t] + 1
			else:
				count[t] = 1
		for t in T:
			if t not in t_ind:
				if t in S:
					t_dict[S.index(t)] = t

				else:
					t_dict[temp] = t
					temp += 1
			t_ind.append(t)
		# print(count)
		# print(t_dict)
		for a in t_dict.keys():
			op = op + t_dict[a]*count[t_dict[a]]
		return op

if __name__ == '__main__':
	s = Solution()
	s1 = "hucw"
	s2 = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
	print(s.customSortString(s1,s2))

				