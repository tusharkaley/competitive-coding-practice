import math

def merge_sort(nums):
	# print(nums)
	if len(nums) <= 1:
		return nums
	else:
		mid = int(math.floor(len(nums)/2))
		# print(nums[:mid+1])
		# print(nums[mid+1:])
		left = merge_sort(nums[:mid])
		right = merge_sort(nums[mid:])

	return merge(left, right)


def merge(left, right):
	nums = list()
	while left or right:
		if not left:
			if right:
				while right:
					nums.append(right.pop(0))
		else:
			if not right:
				while left:
					nums.append(left.pop(0))
		if left and right:
			if left[0]<= right[0]:
				nums.append(left.pop(0))
			else:
				nums.append(right.pop(0))
	return nums


def insertion_sort(nums):
	for i in range(len(nums)):
		smallest = nums[i]
		smallest_ind = i
		for j in range(i,len(nums)):
			if nums[j]<smallest:
				smallest = nums[j]
				smallest_ind = j
		nums[i], nums[smallest_ind] = nums[smallest_ind], nums[i]
	return nums

def radix_sort(nums):
	
if __name__ == '__main__':
	l1 = [1]
	l2 = [0]
	l3 = [9,8,7,6,5,4,3,2,1]
	# print(merge(l1,l2))
	# print(merge_sort(l3))
	print(insertion_sort(l3))



