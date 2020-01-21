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
		while nums2:
			# print(nums2)
			if num1_pointer == boundry:
				break
			if nums1[num1_pointer] < t:
				num1_pointer += 1
			else:
				temp = nums1[num1_pointer]
				nums1[num1_pointer:] = [0] + nums1[num1_pointer:-1]
				nums1[num1_pointer] = t
				t = nums2.pop(0)
				boundry += 1
				num1_pointer += 1
		if nums2:
			nums1[num1_pointer:] = [t] + nums2
		else:
			print("test")
			temp = nums1[num1_pointer]
			nums1[num1_pointer:] = [0] + nums1[num1_pointer:-1]
			nums1[num1_pointer] = t