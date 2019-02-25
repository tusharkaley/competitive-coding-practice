# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # THIS WAS REALLY REALLY COMPLICATED AS OPPOSED TO THE STRAIGHTFORWARD SOLUTION GIVEN BY THE UPLOADER
    # def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    #     t1_list = self.traverse_tree_level_by_level(t1)
    #     t2_list = self.traverse_tree_level_by_level(t2)
    #     len_max = max(len(t1_list), len(t2_list))
    #     op_list = list()
        
    #     print(t1_list)
    #     print(t2_list)
    #     print(len_max)
    #     for i in range(0,len_max):
    #         if t1_list[i]!=None and t2_list[i]!=None:
    #             op_list.append(TreeNode(t1_list[i].val+t2_list[i].val))
    #         elif t1_list[i]==None and t2_list[i]!=None:
    #             op_list.append(TreeNode(t2_list[i].val))
    #         elif t1_list[i]!=None and t2_list[i]==None:
    #             op_list.append(TreeNode(t1_list[i].val))
    #         else:
    #             op_list.append(None)
    
    #     output = self.get_root(op_list)
    #     return output
    # def height(self,root):
    #     if root == None:
    #         return -1
    #     else:
    #         return 1+max(self.height(root.left), self.height(root.right)) 
    # def traverse_tree_level_by_level(self,root):
    #     count = 0
    #     bst_list = list()
    #     bst_list.append(root)
    #     i = 0
    #     h = self.height(root)
    #     while(count<h):
    #         for j in range(i, len(bst_list)):
    #             if bst_list[j] != None:
    #                 bst_list.append(bst_list[j].left)
    #                 bst_list.append(bst_list[j].right)
    #         i = i + int(math.pow(2,count))
    #         count = count + 1
    #     return bst_list
    # def get_root(self,list_nodes):
    #     for i in range(0, int((len(list_nodes)/2))):
    #         list_nodes[i].left = list_nodes[2*i + 1]
    #         list_nodes[i].right = list_nodes[2*i + 2]
    #     return list_nodes[0]

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
        
        