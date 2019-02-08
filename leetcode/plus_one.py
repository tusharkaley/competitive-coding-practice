class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        try:
        	op = list()
        	for i in range(len(digits)-1, -1,-1):
        		digits[i] = digits[i]+1
        		if digits[i]==10:
        			digits[i] = 0
        		else:
        			op = digits
        			break
        		if i==0:
        			op = [1] + digits;
        	return op 

        except Exception as e:
        	raise e

if __name__ == '__main__':
	s = Solution()
	ip = [1]
	print(s.plusOne(ip))