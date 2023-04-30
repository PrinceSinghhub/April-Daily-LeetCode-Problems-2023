class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, m = len(words[0]), len(target)
        maps = [Counter() for _ in range(n)]
        for word in words:
            for i, c in enumerate(word):
                maps[i][c] += 1
        @cache
        def dp(i, j):
            if j >= m: return 1
            if i >= n: return 0
            v = maps[i][target[j]]
            return dp(i + 1, j) + dp(i + 1, j + 1) * v
        return dp(0, 0) % (10 ** 9 + 7)