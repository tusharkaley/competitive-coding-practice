# Complete the countSwaps function below.
def countSwaps(a):
	swap_count = 0
	limit = len(a)
	i = 0
	j = 1
	while i<limit-1:
		while j < limit:
			if a[i]>a[j]:
				a[i],a[j] = a[j],a[i]
				swap_count = swap_count +1
			i = i + 1
			j = j + 1
		limit = limit - 1
		i=0
		j=1 
	print("Array is sorted in {} swaps.".format(swap_count))
	print("First Element: {}".format(a[0]))
	print("Last Element: {}".format(a[-1]))
if __name__ == '__main__':
	ip = [3,2,1]
	countSwaps(ip)


