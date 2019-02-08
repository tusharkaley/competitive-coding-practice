def solution(S, K):
    # write your code in Python 3.6
    try:
    	test = S.replace("-", "")
    	str_len = len(test)
    	output = ""
    	first_block = str_len % K
    	if first_block!=0:
    		output = test[0:first_block]+ "-"
    	count = 0
    	fb = True
    	i=first_block
    	while i<len(test):
    		if count == K:
    			output = output + "-"
    			count = 0
    		else:
    			output = output + test[i].upper()
    			count = count + 1
    			i = i + 1
    	return output
    except Exception as e:
    	raise e
    
if __name__ == '__main__':
	print(solution("2-4A0r7-4k" , 4))