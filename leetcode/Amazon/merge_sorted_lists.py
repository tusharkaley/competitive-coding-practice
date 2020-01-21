# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        prev_node = ListNode(0)
        first_node = prev_node
        while l1 and l2:
            node = ListNode(0)
            if l1.val< l2.val:
                node.val = l1.val
                l1 = l1.next
            else:
                node.val = l2.val
                l2 = l2.next
            prev_node.next = node
            prev_node = node
        prev_node.next = l1 or l2


        return first_node.next