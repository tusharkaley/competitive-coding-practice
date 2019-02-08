class Solution:
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		two_sum_dict = dict()

		for i in range(0,len(nums)):
			for j in range(i+1,len(nums)):
				temp_sum = nums[i]+nums[j]
				if temp_sum in two_sum_dict:

					if [nums[i], nums[j]] not in two_sum_dict[temp_sum]:
						two_sum_dict[temp_sum].append([i, j])
				else:
					two_sum_dict[temp_sum] = [[i, j]]
		out= list()
		two_sum_keys = list(two_sum_dict.keys())
		
		for i in range (0,len(two_sum_keys)):
			if target-two_sum_keys[i] in two_sum_dict:
				out = self.generate_perms(two_sum_dict[two_sum_keys[i]], two_sum_dict[target-two_sum_keys[i]], out)
				two_sum_dict.pop(two_sum_keys[i]) 
		output = list()
		for li in out:
			temp = list()
			for index in li:
				temp.append(nums[index])
			temp.sort()
			if temp not in output:
				output.append(temp)
		return (output)
	
	def generate_perms(self,list1, list2, out):
		
		
		for i in range(0,len(list1)):
			for j in range(0, len(list2)):
				temp = list(set(list1[i] + list2[j]))
				temp.sort()
				if temp not in out and len(temp)==4:
					out.append(temp)
		return out

if __name__ == '__main__':
	s = Solution()
	A=[-5,5,4,-3,0,0,4,-2]


	print(s.fourSum(A,4))


	 #  [-1,  0, 0, 1],
  # [-2, -1, 1, 2],
  # [-2,  0, 0, 2]

  # [[-2, 0, 1, 1], [-1, 0, 0, 1], [-2, -1, 1, 2], [-1, -1, 0, 2], [-2, 0, 0, 2]]

