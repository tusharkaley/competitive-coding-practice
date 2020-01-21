class Solution:
	def threeSum(self, nums):
		op = list()
		two_sum = dict()
		nums.sort()
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				temp = nums[i]+ nums[j]
				if temp not in two_sum:
					two_sum[temp] = [(i,j)]
				else:
					two_sum[temp].append((i,j))
		
		for i in range(len(nums)):
			search = (-1)*(nums[i])
			if search in two_sum:
				temp = two_sum[search]
				for tup in temp:
					if i not in tup:
						val = [nums[i], nums[tup[0]], nums[tup[1]]]
						val.sort()
						if val not in op:
							op.append(val)
			while i < len(nums)-1 and nums[i] == nums[i+1]:
				i+=1
				
		return op
	# def threeSum(self, nums):
	# 	op = list()
	# 	nums.sort()
	# 	for i in range(len(nums)-2):
	# 		j = i+1
	# 		k = len(nums)-1
	# 		while j<k:
	# 			print(op)
	# 			num_sum = nums[i]+nums[j]+nums[k]
	# 			if num_sum == 0:
	# 				if [nums[i],nums[j],nums[k]] not in op:
	# 					op.append([nums[i],nums[j],nums[k]])
	# 				j += 1

	# 				while j<k and nums[j]==nums[j-1]:
	# 					j=j+1
					
	# 			elif num_sum < 0:
	# 				j += 1
	# 			elif num_sum > 0:
	# 				k -= 1
	# 	return op

if __name__ == '__main__':
	s = Solution()
	ip = [-1, 0, 1, 2, -1, -4]
	print(s.threeSum(ip))
