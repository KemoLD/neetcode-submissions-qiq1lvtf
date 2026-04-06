"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        reg = {}

        def search(head):
            if not head:
                return 
                
            if head in reg:
                return reg[head]
            else:
                curr = Node(head.val)
                reg[head] = curr

                for c in head.neighbors:
                    curr.neighbors.append(search(c))

                return curr

        return search(node)