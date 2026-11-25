# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
9:52
DFS > BFS

'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root and subRoot:
                return False
            if root and not subRoot:
                return False
            if root.val!=subRoot.val:
                return False

            return isSameTree(root.left,subRoot.left) and isSameTree(root.right,subRoot.right)
        
        queue = deque()
        if not root:
            return
        queue.append((root))

        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
            
            
            


        