# https://leetcode.com/problems/binary-tree-paths/submissions/


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        op = list()
        if root:
            return self.find_path(root, "")
        else:
            return []
        
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