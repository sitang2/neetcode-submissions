# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            N = len(q)

            for i in range(N):
                nodes = q.popleft()
                if nodes:
                    level.append(nodes.val)
                    q.append(nodes.left)
                    q.append(nodes.right)
            
            if level:
                res.append(level)
        return res