# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        queue = deque()
        queue.append([root, 0])

        Width = 0

        while len(queue) != 0:
            size = len(queue)
            CurrMinIndex = queue[0][1]

            firstIndex = 0
            lastIndex = 0
            for i in range(size):
                Data = queue.popleft()
                Node = Data[0]
                index = Data[1]

                # for update the our Index
                index = index - CurrMinIndex

                if i == 0:
                    firstIndex = index
                if i == size - 1:
                    lastIndex = index

                if Node.left:
                    queue.append([Node.left, index * 2 + 1])

                if Node.right:
                    queue.append([Node.right, index * 2 + 2])

            Width = max(Width, lastIndex - firstIndex + 1)

        return Width




