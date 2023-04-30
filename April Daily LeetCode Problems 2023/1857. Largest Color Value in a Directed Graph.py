class Solution:
    def largestPathValue(self, colors, edges):
        n = len(colors)
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = []
        dp = [[0] * 26 for _ in range(n)]
        colorvalues = [ord(c) - ord("a") for c in colors]
        for u in range(n):
            if u not in indegree:
                queue.append(u)
                dp[u][colorvalues[u]] = 1

        visited = 0
        while queue:
            u = queue.pop()
            visited += 1

            for v in graph[u]:
                for c in range(26):
                    dp[v][c] = max(dp[v][c], dp[u][c] + (c == colorvalues[v]))
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
                    del indegree[v]
        if visited < n:
            return -1
        return max(max(x) for x in dp)