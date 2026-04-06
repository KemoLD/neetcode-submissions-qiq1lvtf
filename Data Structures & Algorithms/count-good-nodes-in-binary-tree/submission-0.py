# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def calculate(node, maxi):
            if not node:
                return 0

            res = 1 if node.val >= maxi else 0
            newMax = max(maxi, node.val)

            left = calculate(node.left, newMax)
            right = calculate(node.right, newMax)

            return res + left + right

        return calculate(root, root.val)