



def solution(S, E):
	# write your code in Python 3.6
	
	consolidated= list()
	for x, y in zip(S,E):
		consolidated.append((x,y))
	
	sorted_list = sorted(consolidated, key=lambda x:x[1])
	if len(sorted_list) == 0:
		return 0
	num_chairs = 0

	start_min = sorted_list[0][0]
	end_max = sorted_list[0][1]

	for (start, end) in sorted_list:
		
		if start < end_max:
			num_chairs = num_chairs + 1
		if start < start_min:
			start_min = start
		end_max = end
	return num_chairs

if __name__ == '__main__':
	S = [1,2,3,5,7,8]
	E = [2,3,4,6,8,9]
	print(solution(S, E))