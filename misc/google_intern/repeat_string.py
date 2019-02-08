class Solution:
	def check_string_repeat_exists(self, str1, str2):
		try:
			if len(str1) > len(str2):
				if str2 in str1:
					return 0
				else:
					return -1
			else:
				if str1 in str2:
					str_repeat = str1
					count = 1
					for i in range(0, len(str2)-1):
						if str2 in str_repeat:
							return count
						str_repeat = str_repeat + str1
						count = count + 1
					return -1	
				else:
					return -1
		except Exception as e:
			raise e

if __name__ == '__main__':
	s = Solution()
	A ='mnopq'
	B = 'opqmnopqmnopq'
	print(s.check_string_repeat_exists(A, B))