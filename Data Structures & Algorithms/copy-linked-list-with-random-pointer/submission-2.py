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
        
        copies = {}

        def copy(node):
            if not node:
                return None

            if node in copies:
                return copies[node]

            x = Node(node.val)
            copies[node] = x

            x.next = copy(node.next)
            x.random = copy(node.random)
            return x

        return copy(head)