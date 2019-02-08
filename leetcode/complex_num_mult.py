class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        try:
        	op_real = 0
        	op_img = 0
        	a_list = a.split("+")
        	b_list = b.split("+")
        	for a_num in a_list:
        		for b_num in b_list:
        			if 'i' in a_num:
        				if 'i' not in b_num:
	        				temp = a_num.split('i')[0]
	        				op_img = op_img + int(temp)*int(b_num)
	        			else:
	        				op_real= op_real - int(a_num.split('i')[0])*int(b_num.split('i')[0])
        			elif 'i' in b_num:
        				op_img = op_img + int(b_num.split('i')[0])*int(a_num)
        			else:
        				op_real= op_real + int(b_num)*int(a_num)
        	return "%s+%si" %(op_real, op_img)
        except Exception as e:
        	raise e

if __name__ == '__main__':    		
	s = Solution()
	a = "1+-1i"
	b = "1+-1i"
	tar = 0
	print(s.complexNumberMultiply(a, b))