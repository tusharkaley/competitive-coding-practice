# class Solution:
# 	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
# 		"""
# 		Do not return anything, modify nums1 in-place instead.
# 		"""
# 		num_1_pointer = 0
# 		num_2_pointer = 0
# 		# nums1.extend(nums)
# 		changed = False
# 		for j in range(m,len(nums1)):
# 			changed = True
# 			nums1[j] = float("inf")
# 		if changed:
# 			while num_2_pointer < n:
				
# 				if nums1[num_1_pointer]<nums2[num_2_pointer]:
# 					num_1_pointer = num_1_pointer + 1
# 				else:

# 					nums1[num_1_pointer:] = [nums2[num_2_pointer]]+nums1[num_1_pointer:-1]
# 					num_2_pointer = num_2_pointer + 1
# 					num_1_pointer = num_1_pointer + 1
class Solution:
	def merge(self, nums1, m, nums2, n):
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		num1_pointer = 0
		if len(nums2) ==0:
			return
		t = nums2.pop(0)
		boundry = m
		while True:
			# print(nums2)
			if num1_pointer == boundry:
				break
			if nums1[num1_pointer] < t:
				num1_pointer += 1
				continue
			else:
				temp = nums1[num1_pointer]
				nums1[num1_pointer:] = [0] + nums1[num1_pointer:-1]
				nums1[num1_pointer] = t
				t = nums2.pop(0)
				boundry += 1
				num1_pointer += 1
			if not nums2:
				break
		if nums2:
			nums1[num1_pointer:] = [t] + nums2
		else:
			temp = nums1[num1_pointer]
			nums1[num1_pointer:] = [0] + nums1[num1_pointer:-1]
			nums1[num1_pointer] = t
		print(nums1)

if __name__ == '__main__':
	s = Solution()
	nums1 = [1,2,3,0,0,0]
	m = 1
	nums2 = [5,6,7]
	n = 1
	s.merge(nums1, m , nums2, n)














