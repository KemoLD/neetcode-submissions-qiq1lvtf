# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        def iterate(head):
            if not head:
                return

            iterate(head.left)
            res.append(head.val)
            iterate(head.right)
        
        iterate(root)
        return res[k-1]