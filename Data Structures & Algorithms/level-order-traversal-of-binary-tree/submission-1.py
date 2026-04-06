# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        
        def search(node, index):
            if not node:
                return

            if len(res) == index:
                res.append([])

            res[index].append(node.val)
            search(node.left, index+1)
            search(node.right, index+1)

        search(root, 0)
        return res