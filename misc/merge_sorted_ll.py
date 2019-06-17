class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        prev_node = ListNode(0)
        first_node = prev_node
        while l1 or l2:
            node = ListNode(0)
            if l1 and l2:
                if l1.val< l2.val:
                    node.val = l1.val
                    l1 = l1.next
                else:
                    node.val = l2.val
                    l2 = l2.next
                prev_node.next = node
                prev_node = node
                continue
                
            if l1 and not l2:
                node.val = l1.val
                l1 = l1.next
                prev_node.next = node
                prev_node = node
                continue
                
            if l2 and not l1:
                node.val = l2.val
                prev_node.next = node
                prev_node = node
                l2 = l2.next

        return first_node.next
                
if __name__ == '__main__':

	t = ListNode(1)
	t2 = ListNode(2)
	t4 = ListNode(4)
	t1 = ListNode(1)
	t3 = ListNode(3)
	t42 = ListNode(4)
	t.next = t2
	t2.next = t4
	t1.next = t3
	t3.next = t42

	s = Solution()

	print(s.mergeTwoLists(t, t1).val)

