# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def closestValue(self, root: TreeNode, target: float) -> int:
    #     while True:
            
    #         diff_root = abs(root.val - target)
    #         diff_left = math.inf
    #         diff_right = math.inf
    #         if root.left:
    #             diff_left = abs(root.left.val - target)
    #         if root.right:
    #             diff_right = abs(root.right.val - target)
    #         if  diff_root< diff_left and diff_root< diff_right:
    #             return self.check_smallest(root, target)

    #         elif diff_left < diff_root and diff_left < diff_right:
    #             root = root.left
    #         elif diff_right < diff_root and diff_right < diff_left:
    #             root = root.right
    # def check_smallest(self, root, target):
    #     left_largest =  0
    #     right_smallest = 0
    #     org_root = root
    #     root = org_root.left
    #     while True:
    #         if root.right:
    #             root = root.right
    #             continue
    #         else:
    #             left_largest = root.val
    #             break
    #     root = org_root.right
    #     while True:
    #         if root.left:
    #             root = root.left
    #             continue
    #         else:
    #             right_smallest = root.val
    #             break
    #     diff_root = abs(root.val - target)
    #     diff_left = abs(left_largest - target)
    #     diff_right = abs(right_smallest - target)
        
        
    #     if  diff_root< diff_left and diff_root< diff_right:
    #         return root.val
    #     elif diff_left < diff_root and diff_left < diff_right:
    #         return left_largest
    #     elif diff_right < diff_root and diff_right < diff_left:
    #          return right_smallest
        
        
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return None
        ret_val = root.val
        while root:
            if root.val == target:
                return root.val        
            elif abs(root.val-target)<abs(ret_val-target):
                ret_val = root.val
            if (target < root.val):
                root = root.left
            elif (target > root.val):
                root = root.right
        return ret_val
                
                        
                