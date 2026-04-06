# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        q = deque()
        q.append(root)

        while q:
            tmp = []
            length = len(q)
            for _ in range(length):
                x = q.popleft()
                if x:
                    q.append(x.left)
                    q.append(x.right)
                    tmp.append(x.val)
            if tmp:
                res.append(tmp)

        return res
