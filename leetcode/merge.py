class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		num_1_pointer = 0
		num_2_pointer = 0
		# nums1.extend(nums)
		changed = False
		for j in range(m,len(nums1)):
			changed = True
			nums1[j] = float("inf")
		if changed:
			while num_2_pointer < n:
				
				if nums1[num_1_pointer]<nums2[num_2_pointer]:
					num_1_pointer = num_1_pointer + 1
				else:

					nums1[num_1_pointer:] = [nums2[num_2_pointer]]+nums1[num_1_pointer:-1]
					num_2_pointer = num_2_pointer + 1
					num_1_pointer = num_1_pointer + 1
