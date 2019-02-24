


def compressedString(message):
	# Write your code here
	op = ""
	count = 1
	last_elem = ""
	for i in range(1,len(message)):
		if message[i]== message[i-1]:
			count = count + 1
			
		else:
			if count!=1:
				op = op + message[i-1] + str(count)
				count = 1
			else:
				op = op + message[i-1]

	if i == len(message)-1:
		if count!=1:
				op = op + message[i] + str(count)
				count = 1
		else:
			op = op + message[i]

	return op

		

if __name__ == '__main__':


	result = compressedString("abc")
	print(result)
