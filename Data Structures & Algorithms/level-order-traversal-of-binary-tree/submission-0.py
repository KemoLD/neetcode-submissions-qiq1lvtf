# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        stack = collections.deque()
        stack.append(root)
        result = []

        while stack:
            length = len(stack)
            tmp = []

            for i in range(length):
                x = stack.popleft()

                if not x is None:
                    tmp.append(x.val)
                    if x.left:
                        stack.append(x.left)
                    if x.right:
                        stack.append(x.right)

            result.append(tmp)

        return result

        