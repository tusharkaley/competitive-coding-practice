class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """	
        sort_list = self.sorted_list(root, R)
        sum_list = 0
        for i in range(len(sort_list)-1,-1,-1):
            if sort_list[i] >= L and sort_list[i] <= R:
                sum_list = sum_list + sort_list[i]
        return sum_list

    def sorted_list(self, root, R):
        res = list()
        if root:
            res = self.sorted_list(root.left, R)
            res.append(root.val)
            res = res + self.sorted_list(root.right, R)
        return res