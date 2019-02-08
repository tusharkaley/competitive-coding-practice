class Solution:
	# def maxArea(self, height):
	# 	"""
	# 	:type height: List[int]
	# 	:rtype: int
	# 	"""
	# 	try:
	# 		area = 0

	# 		for i in range(0,len(height)):
	# 			for j in range(i+1, len(height)):
	# 				if area < ((j-i)*min(height[i], height[j])):
	# 					area = (j-i)*min(height[i], height[j])
	# 		return area
	# 	except Exception as e:
	# 		raise e
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		try:
			start = 0
			end = len(height)-1
			area = 0
			while start < end:
				temp_area = (end - start) * min(height[start], height[end])
				area = temp_area if temp_area > area else area
				if height[start] < height[end]:
					start = start + 1
				else:
					end = end - 1 
			return area
		except Exception as e:
			raise e     
if __name__ == '__main__':			
	s = Solution()
	ip = [2,3,4,5,18,17,6]
	print(s.maxArea(ip))