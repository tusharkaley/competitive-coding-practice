import math
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
        	position = self.binary_search(nums, target, 0, len(nums)-1)
        	return position
        except Exception as e:
        	raise e
    def binary_search(self, nums, target, start, end):
    	try:

    		mid_way = int(math.floor((start+end)/2))

    		if nums[mid_way] == target:
    			return mid_way
    		if end - start == 1 or end - start == 0:
    			if target < nums[end]:
    				if target < nums[start]:
    					return start
    				else:
    					return end
    			if target > nums[end]:
    				return end+1
    			if target == nums[end]:
    				return end
    			if target == nums[start]:
    				return start
    		if target > nums[mid_way]:
    			return self.binary_search(nums, target, mid_way, end)
    		elif target < nums[mid_way]:
    			return self.binary_search(nums, target, 0, mid_way)
    	except Exception as e:
    		raise e

if __name__ == '__main__':    		
	s = Solution()
	ip = [1,3, 5, 6]
	tar = 0
	print(s.searchInsert(ip, tar))

