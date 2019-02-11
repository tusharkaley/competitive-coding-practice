import math
def hourglassSum(arr):
	maxx = calc_sum(arr, 0, 0)
	for i in range(len(arr)-2):
		for j in range(len(arr[0])-2):
			temp = calc_sum(arr, i, j)
			if temp > maxx:
				maxx = temp
	return maxx
def calc_sum(arr, i, j):
	sum = 0
	sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j]+ arr[i+2][j+1] + arr[i+2][j+2]
	return sum

if __name__ == '__main__':
	ip = [[0,1,1,1,1],[1,0,0,0,1],[1,1,0,1,0], [0,1,0,1,1],[0,1,1,1,0]]
	# ip = [[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0]]
	print(hourglassSum(ip))