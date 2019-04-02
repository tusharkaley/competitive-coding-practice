# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, x):
#	self.val = x
#	self.left = None
#	self.right = None

class Solution:
	def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
					if count % 2!=0:
						temp_list.reverse();
					op_list.append(temp_list)
					temp_list= list()
					temp_list.append(node.val)
					count = count + 1
				else:
					temp_list.append(node.val)
				
		if temp_list:
			if (count) % 2!=0:
				temp_list.reverse();
			op_list.append(temp_list)

		return(op_list)