"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
	def cloneGraph(self, node):

		if node == None:

			return None

		GraphClone = {}

		def DFS(node):

			if node in GraphClone:

				return GraphClone[node]

			copy_node = Node(node.val)

			GraphClone[node] = copy_node

			for neighbor in node.neighbors:

				copy_node.neighbors.append(DFS(neighbor))

			return copy_node

		return DFS(node)