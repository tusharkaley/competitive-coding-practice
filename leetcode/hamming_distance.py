class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        try:
        	xbin = bin(x)[2:]
        	ybin = bin(y)[2:]
        	xbin_new = "0"*(len(ybin)) + xbin
        	ybin_new = "0"*(len(xbin)) + ybin
        	
        	count = 0
        	for x, y in zip(xbin_new, ybin_new):
        		if x == y:
        			continue
        		else:
        			count = count + 1
        	return count
        except Exception as e:
        	raise e

if __name__ == "__main__":
    s = Solution()
    x = 1
    y = 4

    print(s.hammingDistance(x, y))
