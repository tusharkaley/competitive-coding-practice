# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
    	head_pointer = head
    	if not head:
    		return head_pointer
    	temp = head.next
    	while temp:
    		if head.val== temp.val:
    			temp = temp.next
    			head.next = None
    		else:
    			head.next = temp
    			head = temp
    			temp = head.next
    	return head_pointer
        