# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(rootp, rootq):
            if not rootp and not rootq:
                return True
            if rootp and not rootq:
                return False
            if rootq and not rootp:
                return False
            if rootp.val!=rootq.val:
                return False

            left = dfs(rootp.left, rootq.left)
            right = dfs(rootp.right, rootq.right)

            return left and right
        res = dfs(p, q)
        return res
            

            
        