from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        res = []
        freq_map = defaultdict(int)
        for i in range(len(nums) + 1):
            bucket.append([])
        for n in nums:
            freq_map[n] += 1
        for num, cnt in freq_map.items():
            bucket[cnt].append(num)
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        