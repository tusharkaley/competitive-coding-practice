def dfs_island(i,j,land, op):

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
            op = dfs_island(i,j-1,land, op)
            
        if right == 1: 
            op = dfs_island(i,j+1,land, op)
            
        if top == 1:

            op = dfs_island(i-1,j,land, op)
            
        if bottom == 1:

            op = dfs_island(i+1,j,land, op)
        return op
if __name__ == '__main__':
    test = [[1,0],[1,1]]
    op = list()
    print(dfs_island(0,0,test,op))