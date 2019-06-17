class Solution:
    def findLengthOfLCIS(self, nums):
    	max_len = 0
    	temp_max = 0
    	for i in range(len(nums)):
    		if i == 0:
    			temp_max = 1
    			max_len = 1
    		else:
    			if nums[i]> nums[i-1]:
    				temp_max+=1

    			else:
    				if temp_max>max_len:
    					max_len = temp_max
    					temp_max = 1
    	if temp_max!=0:
    		if temp_max>max_len:
    					max_len = temp_max
    	return max_len
if __name__ == '__main__':
	s = Solution()
	nums = [1,3,5,4,7]
	# nums = []
	nums = [1,3,5,4,2,3,4,5]
	print(s.findLengthOfLCIS(nums))