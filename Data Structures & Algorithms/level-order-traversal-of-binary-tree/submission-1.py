# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def dfs(depth, root):
            if not root:
                return

            res[depth].append(root.val)
            dfs(depth+1, root.left)
            dfs(depth+1, root.right)

            return
        
        dfs(0, root)

        return list(res.values())




        