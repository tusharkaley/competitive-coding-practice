class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
        	if i % 2 == 0:
        		s = s+nums[i]
        return s



if __name__ == '__main__':
	s = Solution()
	flowerbed = [3,4,2,1]
	n = 0
	print(s.arrayPairSum(flowerbed))