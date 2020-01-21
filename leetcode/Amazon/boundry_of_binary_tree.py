# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        def get_left(node, left):
            left.append(node.val)
            if node.left:
                get_left(node.left, left)
            elif node.right:
                get_left(node.right, left)
            else:
                left.pop()
        def get_right(node, right):
            right.append(node.val)
            if node.right:
                get_right(node.right, right)
            elif node.left:
                get_right(node.left, right)
            else:
                right.pop()
        def get_leaves(node, leaves):
            if node.left is None and node.right is None:
                leaves.append(node.val)
            if node.left:
                get_leaves(node.left, leaves)
            if node.right:
                get_leaves(node.right, leaves)
           
            
            
        left = []
        right = []
        leaves = []
        if not root:
            return root
        if root.left is None and root.right is None:
            return [root.val]
        if root.left:
            get_left(root.left, left)
        if root.right:
            get_right(root.right, right)
        get_leaves(root, leaves)
        right = right[::-1]
        
        return [root.val]+left+leaves+right