import math
class Solution:
	def deckRevealedIncreasing(self, deck):
		"""
		:type deck: List[int]
		:rtype: List[int]
		"""
		try:
			deck.sort(reverse=True)
			output_list = [deck[0]]
			counter = 0
			for i in range(1,len(deck)):
				output_list.append(deck[i])
				last_elem = output_list[0]
				output_list = output_list[1:]
				output_list.append(last_elem)
			output_list.reverse()
			last_elem = output_list[0]

			output_list = output_list[1:]

			output_list.append(last_elem)
			
			return output_list
		except Exception as e:
			raise e

if __name__ == '__main__':
	s = Solution()
	flowerbed = [17,13,11,2,3,5,7]
	n = 0
	print(s.deckRevealedIncreasing(flowerbed))