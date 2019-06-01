# **********Arrays start**********

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

# If we take XOR of zero and some bit, it will return that bit
 # a xor 0=a
# If we take XOR of two same bits, it will return 0
# a xor a=0
# a xor b xor a=(a xor a) xor b=0 xor b=b
# https://leetcode.com/problems/single-number/solution/
def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
# **********Arrays end**********

# **********TREE START**********
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

# Code to get level by level list of nodes of a binary tree 
def traverse_tree_stack(root):
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

# Code to get level by level list of nodes of a tree with a definition that looks like this ->
# Definition for a Node.
# class Node:
#     def __init__(self, val, children):
#         self.val = val
#         self.children = children

def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                for nd in node.children:
                   stack.append((nd, level+1))
                
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

        return op_list

# Traverse the tree in zig zag order level by level
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
# Calculate sum of ALL left elements
def rec_left_node_sum(self,root, left_sum)->int:
        if not root:
            return left_sum
        if root.left == None and root.right == None:
            return left_sum
        
        
        if root.left:
            left_sum = left_sum + root.left.val
            left_sum = self.rec_sum(root.left, left_sum) 
        if root.right:
            left_sum = self.rec_sum(root.right, left_sum)
        return  left_sum

# Calculate sum of ALL left LEAFs
def rec_left_leaf_sum(self,root, left_sum)->int:
        if not root:
            return left_sum
        
        if root.left == None and root.right == None:
            return left_sum
        
        
        if root.left:
            if root.left.left == None and root.left.right == None:
                left_sum = left_sum + root.left.val
            left_sum = self.rec_sum(root.left, left_sum) 
        if root.right:
            
            left_sum = self.rec_sum(root.right, left_sum)
        return  left_sum

# ALL ROOT TO LEAF PATHS
def find_path(self, root: TreeNode, path) ->List[str]:
        plist = list()
        path = path + str(root.val)
        
        if root.left == None and root.right ==None:
            return [path]
        path = path + "->"
        if root.left:
            plist = plist + self.find_path(root.left, path)
        if root.right:
            plist = plist + self.find_path(root.right, path)
        return plist

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
# Given two trees return a merged tree
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

# Inorder traversal
def inorder(self,root, temp):
        if root == None:
            return temp
        self.inorder(root.left, temp)
        temp.append(root.val)
        self.inorder(root.right, temp)
# **********TREE END**********
# **********Linked List start**********
# Given a linked list representing a number in reverse order convert it to that number
# (2 -> 4 -> 3) => 342
def convert_list_to_num(self, l):
        """
        :type l: ListNode
        :rtype: integer
        """
        num_str = ""
        
        while True:
            if not l:
                break
            else:
                num_str = num_str + str(l.val)
                l = l.next
        num_str = num_str[::-1]
        return int(num_str)

# Given a number convert it to a linked list representing that number in reverse order
# 342 => (2 -> 4 -> 3)
def convert_num_to_list(self, num):
    """
    :type num: integer
    :rtype: ListNode
    """
    num_str = str(num)[::-1]
    l= ListNode(0)
    first = True
    l1 = ListNode(0)
    num_str_len = len(num_str)
    count = 0
    for ch in num_str:
        count = count + 1
        if first:
            l.val = int(ch)
            if count < num_str_len:
               l.next = l1
            first = False
        else:
            
            l2 = ListNode(0)
            l1.val = int(ch)
            if count < num_str_len:
                l1.next = l2
                l1 = l2
                
    return l 
# https://leetcode.com/problems/add-two-numbers/submissions/
# Given a two numbers represented as a reversed linked list return their sum
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(0)
        p = l1
        q = l2
        curr = temp
        prev = ListNode(0)
        carry = 0
        while p!= None or q!= None:
            x = p.val if p!= None else 0
            y = q.val if q!= None else 0
            sum = x + y + carry
            carry = int(sum / 10)
            curr.val = sum % 10
            
            curr.next = ListNode(0)
            prev = curr
            curr = curr.next
            if p!= None:
                p = p.next
            if q!= None:
                q = q.next
        if carry> 0:
            curr.val = carry
        else:
            prev.next = None
        return temp
# **********Linked List end**********

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

