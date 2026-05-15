from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        result = []
        for key, value in count.items():
            if value > n//3:
                result.append(key)
                
        return result