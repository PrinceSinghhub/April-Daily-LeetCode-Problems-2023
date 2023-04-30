class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans=0
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            ans=max(ans,(s+i)/(i+1))
        return int(ans)