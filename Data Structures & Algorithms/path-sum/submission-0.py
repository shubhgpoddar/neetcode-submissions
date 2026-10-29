# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = 0
        def track(root, targetSum, result):
            if not root:
                return False
                
            result+=root.val
            if not root.left and not root.right and result==targetSum:
                return True
            if track(root.left, targetSum, result):
                return True
            if track(root.right, targetSum, result):
                return True

            result = result - root.val
            return False
        
        return track(root, targetSum, result)



        
    
        

        