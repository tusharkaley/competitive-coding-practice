class Solution:
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		visited = {}
		for row in range(len(board)):
			for col in range(len(board[0])):
				if self.find_word(row, col, word,board, visited):
					return True
		return False

	def find_word(self, row, col, word, board, visited, pos =0):
		if pos == len(word):
			return True
		if row < 0 or col <0 or row == len(board) or col == len(board[0]) or visited.get((row, col)) or word[pos] != board[row][col]:
			return False

		visited[(row, col)] = True

		op = self.find_word(row-1, col, word, board, visited, pos+1) or self.find_word(row+1, col, word, board, visited, pos+1) or self.find_word(row, col-1, word, board, visited, pos+1) or self.find_word(row, col+1, word, board, visited, pos+1)
		
		visited[(row, col)] = False
		
		return op
		

if __name__ == '__main__':
	s = Solution()
	board =[["C","A","A"],
			["A","A","A"],
			["B","C","D"]]
	word  = "AAB"
	print(s.exist(board, word))