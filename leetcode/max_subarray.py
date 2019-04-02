class Solution:
    def maxSubArray(self, nums):
        highest = nums[0]
        left = 0
        right = 0
        temp_sum = nums[0]
        for i in range(len(nums)):
            temp_sum = temp_sum + nums[i]
            temp_sum = max(temp_sum, nums[i])

            if highest< temp_sum:
                highest = temp_sum
        return

        # for n in nums:
        #     total_sum = total_sum + n
        # while left < 

if __name__ == '__main__':
    s = Solution()
    ip = [-2,1,-3,4,-1,2,1,-5,4]
    s.maxSubArray(ip)