class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        try:
        	ret_nums = [0]*len(A)
        	start = 0
        	end = len(A)-1
        	for num in A:
        		if num%2 == 0:
        			ret_nums[start] = num
        			start = start + 1
        		else:
        			ret_nums[end] = num
        			end = end - 1
        	return ret_nums
        except Exception as e:
        	raise e

if __name__ == "__main__":
    s = Solution()
    nums = [3,1,2,4]
    print(s.sortArrayByParity(nums))
