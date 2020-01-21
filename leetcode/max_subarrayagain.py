class Solution:
	def maxSubArray(self, nums):
		max_so_far = nums[0]
		max_ending_here = nums[0]
		for i in range(1,len(nums)):
			max_ending_here = max(nums[i], max_ending_here + nums[i])
			max_so_far = max(max_ending_here, max_so_far)
		return max_so_far
if __name__ == '__main__':
	s = Solution()
	ip = [-2,1,-3,4,-1,2,1,-5,4]
	print(s.maxSubArray(ip))