class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr = 0
        min_length = float('inf') 
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                min_length = min(min_length, r-l+1)
                curr -= nums[l]
                l += 1
        return 0 if min_length == float('inf') else min_length
