# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Kinda shitty speed but good memory usage.
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        level_list = self.level_order(root)
        diam = 0
        for node in level_list:
            temp_diam = self.height(node.left) + self.height(node.right)
            if temp_diam > diam:
                diam = temp_diam
        return diam
                
    def height(self, root):
        if root == None:
            return 0
        else:
            return 1+max(self.height(root.right), self.height(root.left))
        
    def level_order(self, root):
        queue = list()
        queue.append((root, 0))
        level_list = list()
        while queue:
            node, level = queue.pop(0)    
            if node:
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
                level_list.append(node)
        return level_list
                