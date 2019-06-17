class Solution:
    def generate(self, numRows):
        if numRows==0:
            return []
        elif numRows==1:
            return [[1]]
        else:
            op = [[1],[1,1]]
            for i in range(2,numRows):
                temp = [1]
                seed = op[i-1]
                for j in range(len(seed)-1):
                    temp.append(seed[j]+seed[j+1])
                temp.append(1)
                op.append(temp)
            return op
if __name__ == '__main__':
	s = Solution()
	print(s.generate(0))