from math import log10, floor
class Solution:
    # def isPalindrome(self, x):
    #     if x < 0:
    #     	return False
    #     x = str(x)
    #     while x:
    #     	left = x[0]
    #     	right = str(int(x)%10)
    #     	x = str(x)[1:-1]
    #     	if left!=right:
    #     		return False
    #     return True
    def isPalindrome(self, x):
        if x < 0:
        	return False
        while x:
        	left = int(x // 10**floor(log10(x)))
        	right = x%10
        	temp = x % 10**floor(log10(x))
        	print(temp)
        	print(right)
        	temp = temp//10
        	x = temp

        	if left!=right:
        		return False
        return True
if __name__ == '__main__':
	s = Solution()
	print(s.isPalindrome(1000021))
