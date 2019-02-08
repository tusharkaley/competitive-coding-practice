import traceback
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        try:
        	output = list(S)
        	rev_op = list(S)
        	rev_op.reverse()
        	for i in range(0, len(output)):
        		if output[i].isalpha():
        			output[i] = ""
        	rev_index =0
        	straight_ind = 0
        	while straight_ind < len(rev_op) and rev_index < len(rev_op):
        		if output[straight_ind]== "" and rev_op[rev_index].isalpha():
        			output[straight_ind] = rev_op[rev_index]
        			straight_ind = straight_ind + 1
        			rev_index = rev_index + 1
        		else:
        			if output[straight_ind]!= "":
        				straight_ind = straight_ind + 1
        			if not rev_op[rev_index].isalpha():
        				rev_index = rev_index + 1
        	return "".join(output)
        except Exception as e:
        	traceback.print_exc()
        	raise e
if __name__ == '__main__':
	s = Solution()
	ip = "a-bC-dEf-ghIj"
	print(s.reverseOnlyLetters(ip))