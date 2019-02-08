class Solution:
	def canPlaceFlowers(self, flowerbed, n):
		"""
		:type flowerbed: List[int]
		:type n: int
		:rtype: bool
		"""
		try:
			i = 0
			if n == 0:
				return True
			while i <= len(flowerbed)-1:
				if i < len(flowerbed)-1:
					if flowerbed[i] == 1:
						if flowerbed[i+1] == 0:
							i = i+2
					elif flowerbed[i] == 0:
						if flowerbed[i+1] == 1:
							i = i+3
						else:
							n = n-1
							i = i+2
				else:
					if flowerbed[i] == 0:
						n = n-1
						i = i+1
					else:
						i = i+1
				if n == 0:
					return True
			if n == 0:
					return True
			return False

		except Exception as e:
			raise e
if __name__ == '__main__':
	s = Solution()
	flowerbed = [1,0,0,0,1]
	n = 0
	print(s.canPlaceFlowers(flowerbed, n))
