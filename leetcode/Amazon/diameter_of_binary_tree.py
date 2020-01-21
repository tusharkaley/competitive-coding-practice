# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_h = 1
        def depth(node):
            
            if not node:
                return 0
            
            # print(node.val)
            L = depth(node.left)
            R = depth(node.right)
            self.max_h = max(self.max_h, L+R+1)
                
            return max(L,R)+1
        if not root:
            return 0
        depth(root)
        return self.max_h-1
        