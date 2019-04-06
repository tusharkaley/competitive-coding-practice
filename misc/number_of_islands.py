import copy
class Solution:
    def numIslands2(self, m, n, positions):
        op = list()
        count = 0
        land = [[0]*n for i in range(m)]
        
        for pos in positions:
            i = pos[0]
            j = pos[1]
            cnt, land = self.check_neighbors(i, j, land)
            # print(land)
            # print(cnt)
            count = count + cnt
            # print("retval: {}".format(count))
            
            op.append(count)
        return op
            
    def check_neighbors(self,i,j, matrix):
        # print("i:j : {}:{}".format(i,j))
        left = -10
        top = -10
        right = -10
        bottom = -10
        try:
            if j>0:
                left = matrix[i][j-1]
        except Exception as e:
            pass
        try:
            if i>0:
                top = matrix[i-1][j]
        except Exception as e:
            pass
        try:
            right = matrix[i][j+1]
        except Exception as e:
            pass
        try:
            bottom = matrix[i+1][j]
        except Exception as e:
            pass
        check = list()
        dfs_is = list()
        count = 0
        retval = 0
        # print("left:{}, right:{}, top:{}, bottom:{}".format(left, right, top, bottom))
        if left == 1:
            check.append((i,j-1))
            
        if right == 1: 
            check.append((i,j+1))
            
        if top == 1:
            check.append((i-1,j))
            
        if bottom == 1:
            check.append((i+1,j))
        temp_matrix = copy.deepcopy(matrix)
        # print(check)
        while check:
            temp = check.pop(0)
            temp_dfs = list()
            temp_dfs =self.dfs_island(temp[0],temp[1],temp_matrix,temp_dfs)
            tmp = list()
            for a in check:
                if a in temp_dfs:
                    tmp.append(a)
            check = list(set(check)-set(tmp))

            count = count + 1
        # print("count")
        # print(count)
        if count == 1:
            retval = 0
        else:
            retval = count - 1
            retval = -1 * retval
        
        matrix[i][j] = 1
        return retval, matrix
    
    def dfs_island(self,i,j,land, op):
        land[i][j] = -1
        if (i,j) not in op:
            op.append((i,j))
        else:
            return op
        left = -10
        top = -10
        right = -10
        bottom = -10
        try:
            if j>0:
                left = land[i][j-1]
        except Exception as e:
            pass
        try:
            if i>0:
                top = land[i-1][j]
        except Exception as e:
            pass
        try:
            right = land[i][j+1]
        except Exception as e:
            pass
        try:
            bottom = land[i+1][j]
        except Exception as e:
            pass

        if left == 1:
            op = self.dfs_island(i,j-1,land, op)
            
        if right == 1: 
            op = self.dfs_island(i,j+1,land, op)
            
        if top == 1:

            op = self.dfs_island(i-1,j,land, op)
            
        if bottom == 1:

            op = self.dfs_island(i+1,j,land, op)
        return op

if __name__ == '__main__':
    s = Solution()
    m =3
    n = 3
    # ip = [[0,0],[0,1],[1,2],[2,1]]

    ip = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
    # ip = [[0,0],[1,1],[0,1]]
    print(s.numIslands2(m,n,ip))