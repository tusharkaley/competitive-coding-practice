def longest_palindromic_substr(s):
	len_s =len(s)
	grid = [[False]*len_s for i in range(len_s)]
	longest_len = 0
	longest_pal = ""
	for i in range(len_s-1, -1, -1):
		for j in range(len_s-1, -1, -1):
			if i>j:
				continue
			elif j==i+1:
				grid[i][j] = s[i]==s[j]
			elif i==j:
				grid[i][j] = True
			else:
				grid[i][j] = grid[i+1][j-1] and s[i]==s[j]

			if grid[i][j]:
				if (j-i)+1 > longest_len:
					longest_len = (j-i)+1
					longest_pal = s[i:j+1]

	for i in range(len_s):
		for j in range(len_s):
			print grid[i][j],
		print("")
	return longest_pal

if __name__ =="__main__":
	ip = "babad"
	print(longest_palindromic_substr(ip))