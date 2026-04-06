"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        c = { None: None}

        curr = head
        while curr:
            c[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            node = c[curr]
            node.next = c[curr.next]
            node.random = c[curr.random]
            curr = curr.next

        return c[head]