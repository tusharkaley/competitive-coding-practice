def merge_ints(inter):
	
	j = 1
	
	op = []
	if len(inter) <= 1 :
		return inter
	inter.sort(key = lambda x: x[0])
	temp = inter[0]
	while j< len(inter):

			if temp[0] <= inter[j][0] and temp[1]>= inter[j][1]:
				j += 1
			elif temp[1]>= inter[j][0]:
			# merge and add merged to op
				temp = [temp[0], inter[j][1]]
				j += 1
			else:
				# add both i to op and move both i and j by 1
				op.append(temp)
				temp = inter[j]
				j+=1
	op.append(temp)

	return op
if __name__ == '__main__':
	ints = [[1,4],[2,3]]
	ints = [[1,3],[2,6],[8,10],[15,18]]
	print(merge_ints(ints))
		