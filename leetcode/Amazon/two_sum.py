import collections
class Solution:
    def twoSum(self, nums, target):
        store = collections.defaultdict(list)
        for i in range(len(nums)):
        	store[nums[i]].append(i)
        # print(store)
        for i in range(len(nums)):
        	diff = target - nums[i]
        	if diff in store:
        		if diff == nums[i]:
        			if len(store[diff]) == 2:
        				return  store[diff]
        			else:
        				continue
        		else:
        			return [i] + store[diff]

if __name__ == '__main__':
	s = Solution()
	nums = [2,1,1]
	target = 9
	print(s.twoSum(nums, target))
