# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def search(one, two):
            if not one and not two:
                return True

            if (not one and two) or (one and not two):
                return False

            if one.val != two.val:
                return False

            return search(one.left, two.left) and search(one.right, two.right)

        return search(p, q)
        