def flip_signs(s, K):
	limit = 0
	flip_count = 0
	for ch in s:
		if ch == '-':
			if limit ==0:
				flip_count = flip_count + 1
			if limit < K:
				limit = limit+ 1
			else:
				return -1

		if ch == '+':
			limit = 0
	
	return flip_count


if __name__ == '__main__':
	test = ["++++++", "+", "-+-+-+", "+-+-+-", "---+++", "++--", "+--+--+++--++++--", "+++--+++--++--","+++---"]
	for t in test:
		result = flip_signs(t, 2)
		print("{} : {}".format(t,result))
