'''
valid subarray
sum >= target
min length
invalid
sum < target
target = 10, nums = [2,1,5,1,5,3]
Can I make this window smaller and still have it work?
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float("inf")
        curr = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                res = min(res, r - l + 1)
                curr -= nums[l]
                l += 1
        if res == float("inf"):
            return 0
        else:
            return res
            