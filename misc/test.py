def closest(s, queries):
	op = list()
	close_store= [-1] * len(s)

	for query in queries:
		k= q+1
		i = q-1
		if close_store[query] != -1:
			val = close_store[query]
			if val>query:
				k = len(s)
				temp = helper(queries, s, k, i, val)
			elif val < query:
				i = -1
				temp = helper(queries, s, k, i, val)		
			else:
				temp = val
		else:
			temp = helper(queries, s, k, i, val)	

	def helper(q, s, k , i, val):
	# Write your code here

		length = (-1)*(val-q) if (val-q)<0 else (val-q)
		count = 0
		while (i>=0 or k<len(s)):
			if val!= -1:
				if count > length:
					return -1
				if i>=0:
					if s[i] == s[q]:
						return i
				if k<len(s):
					if s[k] == s[q]:
						return k
				k= k+1
				i = i-1
				count = count + 1
			else:	
				if i>=0:
					if s[i] == s[q]:
						return i
				if k<len(s):
					if s[k] == s[q]:
						return k
				k= k+1
				i = i-1
			
		return -1

			
		
	
	return op



if __name__ == '__main__':
	wordsl = ["add", "booook", "break"]
	print(closest(wordsl))