def rotLeft(a, d):
	count = 0
	a_len = len(a)
	op = ""
	while count < a_len:
		op = op + " "+ str(a[d%a_len])
		d= d+1
		count = count+1
	print(op.strip())
		

if __name__ == '__main__':
	arr = [1,2,3,4,5]
	rot = 19
	rotLeft(arr, rot)