# https://leetcode.com/problems/copy-list-with-random-pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        self.visited = {}
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        def get_cloned_node(x):
            if x:
                if x not in self.visited:
                    new_node = Node(x.val,None, None)
                    self.visited[x] = new_node
                return self.visited[x]
            return None
        if not head:
            return head
        new_node = Node(head.val, None, None)
        old_head = head
        self.visited[head] = new_node
        while head:
            new_node.next = get_cloned_node(head.next)
            new_node.random = get_cloned_node(head.random)
            head = head.next
            new_node = new_node.next
        return self.visited[old_head]