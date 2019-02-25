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
# BST
# Height of a binary search tree
def height(root):
	if root == None:
		return 0
	else:
		return 1+max(height(root.left), height(root.right)) 
# I think this breaks for a tree with just the root node
def traverse_tree_level_by_level(root):
	count = 0
	bst_list = list()
	bst_list.append(root)
	i = 0
	h = height(root)
	while(count<h):
		for j in range(i, len(bst_list)):
			if bst_list[j] != None:
				bst_list.append(bst_list[j].left)
				bst_list.append(bst_list[j].right)
		i = i + int(math.pow(2,count))
		count = count + 1
	return bst_list

def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p == None and q!=None) or (p != None and q==None):
            return False
        if p == None and q == None:
            return True
        if p.val !=q.val:
            return False
        else:
            return (self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left))

if __name__ == '__main__':
	matches = [[0]*4 for _ in range(4)]
	matches[0][1] = 6
	matches[1][0] = 8	
	t = TreeNode(8)
	left = TreeNode(6)
	right = TreeNode(6)
	rleft = TreeNode(6)
	lleft = TreeNode(6)
	t.left = left

	t.right = right
	t.left.left = lleft
	t.right.left = rleft
	print(height(t))

	print(traverse_tree_level_by_level(t))
	# check_neighbours(0,0, matches)

