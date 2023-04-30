class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        Len = max(candies)
        res = []
        for i in candies:
            if (i + extraCandies >= Len):
                res.append(True)
            else:
                res.append(False)

        return res