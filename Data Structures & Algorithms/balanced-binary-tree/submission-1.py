# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if any subtree is unbalanced -> return False
        # node: T/F, If true, height = max(left height, right height)

        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            heightLeft = left[1]
            heightRight = right[1]

            if not left[0] or not right[0] or abs(heightLeft - heightRight) > 1:
                return [False, 0]


            heightNode = 1 + max(heightLeft, heightRight)

            return [True, heightNode]

        res = dfs(root)

        return res[0]
            
           

