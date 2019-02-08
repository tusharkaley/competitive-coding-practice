def solution(A):
	# write your code in Python 3.6
	i = 0
	jump = 1
	k = 0
	while i < len(A):
		if jump % 2 == 0:
			diff= math.inf
			for j in range(i+1, len(A)):
				if A[j]>A[i]:
					if diff > A[j]-A[i]:
						jump = j

		else:
			for j in range(i+1, len(A)):
				if A[j]<A[i]:
					if diff > A[i]-A[j]:
						jump = j
		if j == len(A-1):
			k = k + 1
		i = i + 1
	return k
		
if __name__ == '__main__':
	S = [1,2,3,5,7,8]
	E = [2,3,4,6,8,9]
	print(solution(S, E))