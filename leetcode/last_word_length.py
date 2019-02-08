class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = s.split(" ")
        if len(str_list)== 0:
        	return 0
        else:
        	return len(str_list[-1])