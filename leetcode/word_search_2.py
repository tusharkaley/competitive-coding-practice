class Solution:
    def exist(self, board, word):
#         for each word we can do DFS if the first letter matches and we can DFS in all directions till there is a mismatch

        for i in range(len(board)):
            for j in range(len(board[0])):
                # print("{}: {}".format(i,j))
                # print("{}: {}".format(word[0],board[i][j]))
                if word[0] == board[i][j]:
                    if self.search_word(word, 0, board,{}, i, j):
                        return True
        return False

    def search_word(self, word, match, board,visited,i,j):
        left, right, top, bottom = 0,0,0,0
        # print("{}: {}".format(match, len(word)))
        # print("i:j: {}: {}".format(i,j))
        
        if board[i][j] != word[match] or visited.get((i,j)):
            return False
        if match == len(word)-1:
            return True
        visited[(i,j)] = True
        

        if i-1>=0:
            top = board[i-1][j]
        if j-1>=0:
            left = board[i][j-1]
        try:
            right = board[i][j+1]
        except:
            pass
    
        try:
            bottom = board[i+1][j]
        except:
             pass
        chk = False

        if left:
            chk = chk or  self.search_word(word, match+1, board, visited,i, j-1)
            if chk:
                return chk
        
        if right:
            chk = chk or self.search_word(word, match+1, board, visited,i, j+1)
            if chk:
                return chk
        
        if top:
            chk = chk or self.search_word(word, match+1, board, visited,i-1, j)
            if chk:
                return chk
            
        if bottom:

            chk = chk or self.search_word(word, match+1, board, visited,i+1, j)
            if chk:
                return chk
        visited[(i, j)] = False
        return chk
        
        
            
if __name__ == '__main__':
    s = Solution()
    board =[["A","B","C","E"],
            ["S","F","E","S"],
            ["A","D","E","E"]]
    word = "ABCESEEEFS"
    # board = [["A"]]
    # word = "A"
    print(s.exist(board, word))


