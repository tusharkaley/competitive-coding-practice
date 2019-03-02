class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op= list()
        for i in range(0,len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    op.append([nums[i],nums[j],nums[k]])
                    j = j+1
                    while j<k and nums[j]==nums[j-1]:
                        j=j+1
                elif nums[i]+nums[j]+nums[k]<0:
                    j = j+1
                else:
                    k=k-1
        return op

if __name__ == '__main__':
	s = Solution()
	print(s.threeSum([-1, 0, 1, 2, -1, -4]))


