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

def build_heap(A, max):

	for i in range(int(len(A)//2)-1,-1,-1):
		if max:
			A = max_heapify(i, A)
		else:
			A = min_heapify(i, A)
	return (A)

def max_heapify(i, A):
	largest = i
	left  = left_child(i)
	right = right_child(i)
	if left < len(A) and A[largest] < A[left]:
		largest = left
	if right < len(A) and A[largest] < A[right]:
		largest = right
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		A = max_heapify(largest, A)

	return A

def min_heapify(i, A):
	smallest = i
	left  = left_child(i)
	right = right_child(i)
	if left < len(A) and A[smallest] > A[left]:
		smallest = left
	if right < len(A) and A[smallest] > A[right]:
		smallest = right
	if smallest != i:
		A[i], A[smallest] = A[smallest], A[i]
		A = min_heapify(smallest, A)

	return A
def left_child(i):
	return (2*i+1)


def right_child(i):
	return (2*i+2)

def get_k_smallest(k, A):
	heap = build_heap(A, False)
	op = list()
	for i in range(k):
		op.append(heap.pop(0))
		heap = build_heap(heap, False)
	print(op)

def get_k_largest(k, A):
	heap = build_heap(A, True)
	op = list()
	for i in range(k):
		op.append(heap.pop(0))
		heap = build_heap(heap, True)
	print(op)


if __name__ == '__main__':
	l1 = [1]
	l2 = [0]
	l3 = [9,8,7,6,5,4,3,2,1]
	# print(merge(l1,l2))
	# print(merge_sort(l3))
	# print(insertion_sort(l3))
	sorted_list = [1, 2, 3, 4, 5]
	build_heap(l3, False)
	get_k_smallest(3, l3)
	get_k_largest(3, l3)




