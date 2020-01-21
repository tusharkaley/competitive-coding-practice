def bin_search(arr, start, end, target):
	mid = (start+end)//2
	print(arr[start:end+1])
	if arr[mid] == target:
		return mid
	if mid == start or mid == end:
		if arr[start] == target:
			return start
		if arr[end] == target:
			return end
		return -1
	if arr[mid] > target:
		return bin_search(arr, start, mid-1, target)
	else:
		return bin_search(arr, mid+1, end, target)

if __name__ == '__main__':
	ip = [1,2,3,4,5,6,7,8,9,24]
	print(bin_search(ip, 0, len(ip)-1, 1))