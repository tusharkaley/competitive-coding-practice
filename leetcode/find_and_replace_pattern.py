
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        try:
        	pattern_match = list()
        	for word in words:
        		temp_dict = dict()
        		pattern_dict = dict()
        		word_match = True
        		for i in range(0,len(word)):
        			if pattern[i] not in temp_dict:
        				if word[i] not in pattern_dict:
        					temp_dict[pattern[i]] = word[i]
        					pattern_dict[word[i]] = pattern[i]
        				elif pattern_dict[word[i]] != pattern[i]:
        					word_match = False
        					break
        			else:
        				if temp_dict[pattern[i]] == word[i]:
        					continue
        				else:
        					word_match = False
        					break
        		if word_match:
	        		pattern_match.append(word)	
        	return pattern_match
        except Exception as e:
        	raise e

if __name__ == '__main__':    		
	s = Solution()
	words = ["abc","deq","mee","aqq","dkd","ccc"]
	pattern = "abb"
	print(s.findAndReplacePattern(words, pattern))