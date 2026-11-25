# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
11/24 9:25
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = deque()
        queue_q = deque()

        if not p and not q:
            return True
        if not p or not q:
            return False
        queue_p.append((p))
        queue_q.append((q))
        
        while queue_p and queue_q:
            N = len(queue_p)

            for i in range(N):
                node_p = queue_p.popleft()
                node_q = queue_q.popleft()

                if not node_p and not node_q:
                    continue
                
                if not node_p or not node_q or node_p.val!=node_q.val:
                    return False
                queue_p.append(node_p.left)
                queue_q.append(node_q.left)
                queue_p.append(node_p.right)
                queue_q.append(node_q.right)
            
                
        return True

