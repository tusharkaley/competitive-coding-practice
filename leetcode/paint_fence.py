class Solution:
    def numWays(self, n, k):
        
        posts = [0]*n

        posts[0] = 1
        posts[1] = k
        for j in range(2,n):
        	posts[j]= posts[j-1]+posts[j-2]

        return (posts[-1]*k)


if __name__ == '__main__':
	s = Solution()
	print(s.numWays(4,2))