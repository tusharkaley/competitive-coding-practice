# Complete the makeAnagram function below.
def makeAnagram(a, b):
	a_dict = dict()
	count = 0
	for ch in a:
		if ch not in a_dict:
			a_dict[ch]=1
		else:
			a_dict[ch]=a_dict[ch]+1
	print(a_dict)
	for ch in b:
		if ch in a_dict:
			if a_dict[ch]>0:
				count = count + 1
				a_dict[ch]=a_dict[ch]-1
	return (len(a)+len(b)-(2)*count)

def makeAnagram_noextraspace(a, b):
	total = 0
	for let in "abcdefghijklmnopqrstuvwxyz":
		total = total + abs(a.count(let)-b.count(let))
	return total
if __name__ == '__main__':
	print(makeAnagram("cde", "abc"))
	print(makeAnagram_noextraspace("cde", "abc"))
