class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        mod = 10 ** 9 + 7
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                continue
            for j in range(i, len(s)):
                tmp = int(s[i:j + 1])
                if tmp > k:
                    break
                dp[i] += dp[j + 1]
        return dp[0] % mod
