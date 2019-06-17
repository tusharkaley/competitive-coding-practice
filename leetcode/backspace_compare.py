class Solution:
    def backspaceCompare(self, S, T):
    	if self.getRawString(S) == self.getRawString(T):
    		return True
    	else:
    		return False

    def getRawString(self, ip):
    	op =''
    	for i in ip:
    		if i != '#':
    			op = op + i
    		else:
    			op = op[:-1]
    	return op

if __name__ == '__main__':

	s = Solution()
	S = ""
	T = "b"
	print(s.backspaceCompare(S, T))