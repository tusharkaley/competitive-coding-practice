class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        change_store = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print("{}:{}".format(i,j))
                nei = self.check_neighbours(board, i, j)
                if  nei is not None and nei != board[i][j]:
                    change_store[(i,j)] = nei
        print(change_store)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) in change_store:
                    board[i][j] = change_store[(i,j)]
        
        return
    
    def check_neighbours(self, board, i, j):
        shift = ((0,1),(1,0),(0, -1),(-1,0))
        temp_i = i-1
        temp_j = j-1
        direction = 0
        live_count = 0
        for ind in range(8):
            if temp_i in range(len(board)) and temp_j in range(len(board[0])):
                if board[temp_i][temp_j] == 1:
                    live_count += 1
                if ind not in  {2,4,6}:
                    temp_i = temp_i + shift[direction][0]
                    temp_j = temp_j + shift[direction][1]
                
                    
            else:
                if ind not in  {2,4,6}:
                    temp_i = temp_i + shift[direction][0]
                    temp_j = temp_j + shift[direction][1]
                    continue
            if ind in {2,4,6}:
                direction = (direction+1) & 3
                temp_i = temp_i + shift[direction][0]
                temp_j = temp_j + shift[direction][1]
        if board[i][j] == 1 and live_count < 2:
             return 0
        elif board[i][j] == 1 and live_count in {2,3}:
            return 1
        elif board[i][j] == 1 and live_count > 3:
            return 0
        elif board[i][j] == 0 and live_count == 3:
            return 1
            
                    
            