class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
       	try:
       		ascii_list = list()
       		#3 cases 
       		for letter in word:
       			ascii_list.append(ord(letter))
       		
       		#1.All caps ok
       		case_1 = True
       		for asc in ascii_list:
       			if not 65<=asc<=90:
       				case_1 = False
       		#2 all small ok
       		case_2 = True

       		for asc in ascii_list:
       			if not 97<=asc<=122:
       				case_2 = False
       		case_3 = True
       		for i in range(0, len(ascii_list)):
       			if i == 0:
       				if not 65<=ascii_list[i]<=90:
       					case_3= False
       			else:
       				if not 97<=ascii_list[i]<=122:
       					case_3 = False

       		if case_1 or case_2 or case_3:
       			return True
       		else:
       			return False	
       		#3 first caps ok

       	except Exception as e:
       		raise e

if __name__ == '__main__':			
	s = Solution()
	ip = "z"
	print(s.detectCapitalUse(ip))