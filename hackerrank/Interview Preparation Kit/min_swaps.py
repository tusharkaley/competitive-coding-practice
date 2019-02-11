def minimumSwaps(arr):
    swap_count = 0
    smallest = min(arr)
    ind = 0
    while True:        
        if arr[ind]!= ind+1:
            swap_count    = swap_count + 1
            temp = arr[ind]-1
            arr[ind], arr[temp] = arr[temp], arr[ind]
        else:
        	ind = ind + 1
        if ind == len(arr) -1:
        	break

    return swap_count

if __name__ == '__main__':
	a = [1,3,5,2,4,6,7]
	# a = [7, 1, 3, 2, 4, 5, 6]
	# a = [4,3,1,2]
	print(minimumSwaps(a))

