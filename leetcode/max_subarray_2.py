class Solution:
    def maxSubArray(self, nums):
        i = 0
        j = 0
        max_num = nums[0]
        tsum = 0
        while j < len(nums):
        	print(max_num)
        	if nums[j]>max_num and max_num+nums[j] < max_num:
	        	i = j
	        	max_num = nums[j]
        		tsum = max_num
        	else:
        		tsum = tsum + nums[j]
        		if tsum > max_num:
        			max_num = tsum
        	
        	j += 1
        return max_num

if __name__ == '__main__':
	s = Solution()
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	# nums = [-5,-4,-3,-12,-1]
	# nums = [1,2]
	# nums = [1,2,3,4]
	print(s.maxSubArray(nums))