import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        op= list()
        closest = abs(target-(nums[0]+nums[1]+nums[2]))
        op = nums[0]+nums[1]+nums[2]
        for i in range(0,len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k=len(nums)-1
            # print(i)
            # print("***********")
            while j<k:
                # print(abs(target-(nums[i]+nums[j]+nums[k])))
                if (nums[i]+nums[j]+nums[k])==target:
                    if abs(target-(nums[i]+nums[j]+nums[k]))<closest:
                        closest = abs(target-(nums[i]+nums[j]+nums[k]))
                        op = nums[i]+nums[j]+nums[k]
                    j = j+1
                    while j<k and nums[j]==nums[j-1]:
                        
                        j=j+1
                elif (nums[i]+nums[j]+nums[k])<target:
                    if abs(target-(nums[i]+nums[j]+nums[k]))<closest:
                        closest = abs(target-(nums[i]+nums[j]+nums[k]))
                        op = nums[i]+nums[j]+nums[k]
                    j = j+1
                else:
                    if abs(target-(nums[i]+nums[j]+nums[k]))<closest:
                        closest = abs(target-(nums[i]+nums[j]+nums[k]))
                        op = nums[i]+nums[j]+nums[k]
                    k=k-1
            #     print(closest)
            # print("***********")
        return op


