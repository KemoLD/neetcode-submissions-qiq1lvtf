# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(head):

            if not head:
                return None

            tmp = head.left
            head.left = head.right
            head.right = tmp

            invert(head.right)
            invert(head.left)
            return head

        return invert(root)
        