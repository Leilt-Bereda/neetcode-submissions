from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        for key, value in count.items():
            if value > len(nums) / 2:
                return key
