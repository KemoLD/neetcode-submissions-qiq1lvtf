# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            x = None
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node:
                    x = node
                    queue.append(node.left)
                    queue.append(node.right)
            if x:
                result.append(x.val)

        return result