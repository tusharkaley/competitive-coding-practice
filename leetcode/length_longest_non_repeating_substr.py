class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxval = 0
        while len(s) !=0:
            maxval, s = self.partitionString(maxval, s)
        return maxval
    def partitionString(self, currentMax, substr):
    	"""
    	currentMax
    	substr
    	"""
    	try:
    		if len(substr) == 0 or len(substr) == 1:
    			return max(currentMax,len(substr)), ""
    		else:
    			char_dict = dict()
    			max_len = 0
    			count = 0
    			for ch in substr:
    				if ch not in char_dict:
    					char_dict[ch] = count
    					max_len = max_len + 1
    					count = count + 1
    				else:
    					if count-char_dict[ch] != -1:
    						return max(max_len,currentMax), substr[char_dict[ch]+1:]
    					else:
    						return max(max_len, currentMax), substr[count:]
    			if count == len(substr):
    				return max(count, currentMax), ""
    	except Exception as e:
    		raise e

if __name__ == "__main__":
    sol = Solution()
    ip = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(sol.lengthOfLongestSubstring(ip))