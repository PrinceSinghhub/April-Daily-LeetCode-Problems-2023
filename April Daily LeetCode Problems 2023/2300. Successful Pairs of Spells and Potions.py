class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions)
        ans = []
        for s in spells:
            target = (success - 1) // s
            index = bisect.bisect_right(potions, target)
            ans.append(N - index)

        return ans