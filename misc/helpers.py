# 2D Array
# Check neighbours in a 2 D array
# Definition for a binary tree node.
import math
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def check_neighbours(r, c, mat):
	left = -10
	right = -10
	top = -10
	bottom =-10

	try:
		left = mat[r][c-1]
	except Exception as e:
		pass
	try:
		right = mat[r][c+1]
	except Exception as e:
		pass
	try:
		top = mat[r-1][c]
	except Exception as e:
		pass
	try:
		bottom = mat[r+1][c]
	except Exception as e:
		pass
	if left:
		print("left: {}".format(left))
	if right:
		print("right: {}".format(right))
	if top:
		print("top: {}".format(top))
	if bottom:
		print("bottom: {}".format(bottom))
# **********BST END**********
# Height of a binary search tree
def height(root):
	if root == None:
		return -1
	else:
		return 1+max(height(root.left), height(root.right)) 
# I think this breaks for a tree with just the root node 
# YEP THIS IS CRAP 
# def traverse_tree_level_by_level(root):
# 	count = 0
# 	bst_list = list()
# 	bst_list.append(root)
# 	i = 0
# 	h = height(root)
# 	while(count<h):
# 		for j in range(i, len(bst_list)):
# 			if bst_list[j] != None:
# 				bst_list.append(bst_list[j].left)
# 				bst_list.append(bst_list[j].right)
# 		i = i + int(math.pow(2,count))
# 		count = count + 1
# 	return bst_list

def traverse_tree_stack(root):
	count = 0
	i = 0
	stack = [(root, 0)]
	
	op_list = list()
	temp_list = list()
	prev_lev = 0
	while stack:
		node, level = stack.pop(0)
		# print(stack)
		if node: 
			stack.append((node.left, level+1))
			stack.append((node.right, level+1))
			# print(level)
			if prev_lev != level:
				prev_lev = level
				op_list.append(temp_list)
				temp_list= list()
				temp_list.append(node.val)
			else:
				temp_list.append(node.val)
	if temp_list:
		op_list.append(temp_list)

	op_list = op_list[::-1]
	return op_list
# Check if p and q are exactly the same....values and node structure should match
def isSameTree(self, p, q):
        if (p == None and q!=None) or (p != None and q==None):
            return False
        if p == None and q == None:
            return True
        if p.val !=q.val:
            return False
        else:
            return (self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left))


def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        mid = 0
        num_len = len(nums)
        if num_len == 0:
            return None
        if num_len%2 ==0:
            mid = int(num_len/2)-1
        else:
            mid = int(num_len/2)
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return node

# **********BST END**********
if __name__ == '__main__':

	t = TreeNode(8)
	left = TreeNode(6)
	right = TreeNode(5)
	rleft = TreeNode(4)
	lleft = TreeNode(3)
	t.left = left

	t.right = right
	t.left.left = lleft
	t.right.left = rleft
	print(height(t))

	print(traverse_tree_stack(None))
	# check_neighbours(0,0, matches)

