# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # [2, 3]
        res = []
        queue = deque()
        if not root:
            return []
        queue.append(root)

        while(queue):
            right = None
            qlen = len(queue)
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    right = node
                    print(node.val, i)
                    queue.append(node.left)
                    queue.append(node.right)
            if right:
                res.append(right.val)

        return res
        