class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        try:
        	sent_list = S.split(" ")
        	output = list()
        	index = 1
        	for word in sent_list:
        		if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U']:
        			output.append(word + "ma")
        		else:
        			output.append(word[1:] + word[0]+"ma")
        		output[index-1] = output[index-1] + "a"*index
        		index = index + 1

        	return "".join(i + " " for i in output).strip()

        except Exception as e:
        	raise e

if __name__ == '__main__':    		
	s = Solution()
	ip = "I speak Goat Latin"
	tar = 0
	print(s.toGoatLatin(ip))