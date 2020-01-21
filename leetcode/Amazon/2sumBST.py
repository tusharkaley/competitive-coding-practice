class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(root):
            if root.left:
                inorder(root.left)
            sl.append(root.val)
            if root.right:
                inorder(root.right)
        sl = []
        inorder(root)
        i = 0
        j = len(sl)-1
        while i < j:
            s = sl[i] + sl[j]
            if  s == k:
                return True
            elif s > k:
                j-=1
            else:
                i+=1
        return False