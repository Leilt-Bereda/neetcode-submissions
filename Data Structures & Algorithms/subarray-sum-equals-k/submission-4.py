class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = defaultdict(int)
        map[0] = 1
        count = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in map:
                count += map[prefix_sum - k]
            map[prefix_sum] += 1
        return count
#  [2,-1,1,2], k = 2
#  map = 0:1, 2:2, 1:1
#  sum = 4
#  count = 4