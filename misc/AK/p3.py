
def  melon_count(boxes, melons):
    matches =[[0]*len(melons) for _ in range(len(boxes))]
    for i in range(len(boxes)):
    	for j in range(len(melons)):
    		if melons[j]<=boxes[i]:
    			matches[i][j] =1
    maxx = 0
    print(matches)
    for i in range(len(boxes)):
    	for j in range(len(melons)):
    		if matches[i][j]==1:
    			temp = count_diag(matches, i, j)
    			if temp > maxx:
    				maxx = temp
    return maxx
    
def count_diag(matrix, i, j):
	temp_i = i+1
	temp_j = j+1
	count = 1
	# print("i, j : {} {}".format(i,j))
	# print(matrix)
	skipped = False
	while True:
		if temp_i > len(matrix)-1 or temp_j > len(matrix[0])-1:
			break
		if skipped:
			if temp_i+1<len(matrix)-1:
				if matrix[temp_i+1][temp_j]==1:
					temp_i= temp_i + 1
					count=count+1
					skipped=False
					continue

		if matrix[temp_i][temp_j]==1:
			count = count +1
		elif matrix[temp_i][temp_j]==0:
			skipped=True
		temp_i = temp_i + 1
		temp_j = temp_j + 1
	return count


if __name__ == '__main__':

	melons = [1,2,1,2]
	box = [3,2,1]

	result = melon_count(box, melons)
	print(result)
