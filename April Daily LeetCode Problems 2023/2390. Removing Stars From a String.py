class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for c in s:
            if c != '*':
                stk.append(c)
            else:
                stk.pop()
        return "".join(stk)