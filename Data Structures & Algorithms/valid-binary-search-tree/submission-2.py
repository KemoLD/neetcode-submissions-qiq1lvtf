# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def search(curr, mini, maxi):
            if not curr:
                return True

            if curr.val <= mini or curr.val >= maxi:
                return False

            return search(curr.left, mini, curr.val) and search(curr.right, curr.val, maxi)

        return search(root, float("-inf"), float("inf"))
        