class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_count = 0
        for num in nums:
            if (num - 1) not in numSet:
                j = 1
                cnt = 1
                while num + j in numSet:
                    cnt += 1
                    j += 1
                max_count = max(cnt, max_count)
        return max_count