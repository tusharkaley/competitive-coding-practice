# Complete the sherlockAndAnagrams function below.
import math
def sherlockAndAnagrams(s):
	substr_dict =dict()

	offset = 1 
	j = 0
	i = 0
	temp = ""
	f= math.factorial
	while(offset<=len(s)):
		while(j<len(s)):
			j = i + offset
			if s[i:j] != '':
				temp = list(s[i:j])
				temp.sort()
				temp = "".join(temp)
				if temp not in substr_dict:
					substr_dict[temp]= 1
				else:
					substr_dict[temp]= substr_dict[temp] + 1
			i = i + 1
		j = 0
		i = 0

		offset = offset + 1
	count = 0
	test = list(substr_dict.values())
	for val in test:
		if val!=1:
			count = count + (int(f(val)/f(2)/f(val-2)))
	return count

if __name__ == '__main__':
	
	print(sherlockAndAnagrams("momzom"))