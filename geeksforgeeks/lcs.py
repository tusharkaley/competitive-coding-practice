

def find_lcs(a, b):

	first_row = [1] * len(a)
	rows = [1]+[0] * (len(a)-1)
	matrix = [first_row] + [rows] * (len(b) - 1)

	if len(a) == 0 or len(b) == 0:
		return
	else:
		for i in range(1, len(b)):
			for j in range(1, len(a)):
				if a[j] == b[i]:
					matrix[i][j] = 1 + matrix[i-1][j-1]
				else:
					if matrix[i][j-1] > matrix [i-1][j]:
						matrix[i][j] = matrix[i][j-1]
					else:
						matrix[i][j] = matrix[i-1][j]
		return matrix

if __name__ == '__main__':
	a = "LRBBMQBHCDARZOWKKYHIDDQSCDXRJMOWFRXSJYBLDBEFSARCBYNECDYGGXXPKLORELLNMPAPQFWKHOPKMCO"
	b = "QHNWNKUEWHSQMGBBUQCLJJIVSWMDKQTBXIXMVTRRBLJPTNSNFWZQFJMAFADRRWSOFSBCNUVQHFFBSAQXWPQCAC"
	
	print(find_lcs(a, b))

