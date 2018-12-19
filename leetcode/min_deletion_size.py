class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        try:
        	if len(A) <= 1:
        		return 0
        	elif len(A[0]) == 1:
        		return 0
        	else:
        		len_word = len(A[0])
        		
        		count = 0
        		for i in range(0, len_word):
        			first_word = A[0][i]
	        		for word in A:
	        			if ord(first_word) > ord(word[i]):
	        				count = count + 1
	        				break
	        			first_word = word[i]
	        	return count
        except Exception as e:
        	raise e

if __name__ == "__main__":
    s = Solution()
    nums = ["zyx","wvu","tsr"]
    print(s.minDeletionSize(nums))
