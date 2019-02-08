import traceback
matrix = list() 
def lis_main(input_list):
	try:
		

		for i in range(0,len(input_list)):
			matrix.append(len(input_list)*[0])
		for i in range(0,len(input_list)):
			matrix[i][i] = 1
		print matrix
		return longest_increasing_subsequence(0,len(input_list)-1, input_list)
	except Exception as e:
		traceback.print_exc()
		raise e
def longest_increasing_subsequence(start, end, ip_list):
	
	try:
		# print(start)
		print(len(matrix))
		print(len(matrix[0]))
		if matrix[start][end] != 0:
			print(matrix)
			return matrix[start][end]
		else:
			if end - start == 1:
				if ip_list[end] > ip_list[start]:
					matrix[start][end] = 2
				else:
					matrix[start][end] = 1
				
			else:
				if matrix[start][start+1] ==1:
					matrix[start][end] = longest_increasing_subsequence(start+1, end, ip_list)
					return 
				else:
					matrix[start][end] = 1 + longest_increasing_subsequence(start+1, end, ip_list)
			return matrix[start][end]
	except Exception as e:
		traceback.print_exc()
		raise e

if __name__ == '__main__':
	ip = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
	print(lis_main(ip))