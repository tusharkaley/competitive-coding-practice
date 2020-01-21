import math
def search(nums, target):
	if len(nums) == 0:
		return -1

	def search_helper (arr, tar, s, e):
		mid = math.ceil((s+e)//2)
		# if s > e:
		# 	return -1
		if mid in {s,e}:
			if arr[s] == tar:
				return s
			elif arr[e] == tar:
				return e
			else:
				return -1
		if arr[mid] == tar:
			return mid
		if arr[mid] < arr[e]:
			# last part sorted
			if target > arr[mid] and target<= arr[e]:
				return search_helper(arr, tar, mid+1, e)
			else:
				return search_helper(arr, tar, s, mid-1)
		else:
			if target < arr[mid] and target>= arr[s]:
				return search_helper(arr, tar, s, mid-1)	
			else:
				return search_helper(arr, tar, mid+1, e)
			# first part sorted
	return search_helper(nums, target, 0, len(nums)-1)
if __name__ == '__main__':
	ls = [1,2,3,4]
	tar = 0
	tar = 1
	print(search(ls, tar))