

def smallestString(weight):
    # Write your code here
    weight_dict = dict()
    count = 2
    weight_dict['A'] = 1
    for ch in "BCDEFGHIJKLMNOPQRSTUVWXYZ":
    	weight_dict[ch] = count * weight_dict[chr(ord(ch)-1)] + count
    	count = count + 1
    wt_list = list()
    alph_list = list()
    print(weight_dict)
    for key in weight_dict.keys():
    	if weight_dict[key] > weight:
    		break
    	else:
    		alph_list.append(key)
    		wt_list.append(weight_dict[key])

    alph_list.sort()
    wt_list.sort()
    op = list()
    while weight!=0:
    	if weight <  wt_list[-1]:
    		del wt_list[-1]
    		del alph_list[-1]
    	else:
    		weight = weight - wt_list[-1]
    		op.append(alph_list[-1])

    op.sort()
    retVal = ''.join(op)
    return retVal


if __name__ == '__main__':

	result = smallestString(20)
	print(result)
