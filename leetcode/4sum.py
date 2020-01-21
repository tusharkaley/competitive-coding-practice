class Solution:
	def fourSum(self, nums, target):
		nums.sort()
		op = []
		print(nums)
		for i in range(len(nums)-3):
			if i != 0 and nums[i] == nums[i-1]:
				continue

			for j in range(i+1, len(nums)-2):
				if j != i+1 and nums[j] == nums[j-1]:
					print(nums[j])
					continue
				
				l = j+1
				r = len(nums)-1
				while l<r:
					n_sum = nums[i]+ nums[j] + nums[l] + nums[r]
					if n_sum == target:
						op.append([nums[i], nums[j] , nums[l] , nums[r]])
						l += 1
						while l < r and nums[l-1]== nums[l]:
							l += 1
						r -= 1
						while r > l and nums[r+1] == nums[r]:
							r -= 1
						
					elif n_sum < target:
						l += 1
						while l < r and nums[l-1]== nums[l]:
							l += 1
					elif n_sum > target:
						r -= 1
						while r > l and nums[r+1] == nums[r]:
							r -= 1
		return op


if __name__ == "__main__":
	s = Solution()
	ip = [-3,-2,-1,0,0,1,2,3]
	print(s.fourSum(ip, 0))
