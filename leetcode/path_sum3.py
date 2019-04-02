# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution:
	def pathSum(self, root: TreeNode, sum: int) -> int:
		nodes = self.get_all_nodes(root)
		count = 0
		for nd in nodes:
			count = count + self.hasPathSum(nd,sum, 0, 0)
		return(count)

	def get_all_nodes(self, root):
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
					op_list.extend(temp_list)
					temp_list= list()
					temp_list.append(node)
				else:
					temp_list.append(node)
		if temp_list:
			op_list.extend(temp_list)

		return op_list
	def hasPathSum(self, root: TreeNode, sum: int, count: int, current_sum: int) -> int:
		
		if root == None:
			return count
		current_sum = current_sum + root.val
		
		if current_sum == sum:
			count = count + 1

		count =  self.hasPathSum(root.left, sum, count, current_sum)
		count =  self.hasPathSum(root.right, sum, count, current_sum)
		return count