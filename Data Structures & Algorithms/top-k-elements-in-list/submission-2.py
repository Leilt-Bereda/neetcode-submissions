'''
'''
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        res = []
        sortedCount = sorted(count.items(), key=lambda x: x[1], reverse=True)
        #[(1, 3), (3, 2), (2, 1)]
        for i in range(k):
            res.append(sortedCount[i][0])
        return res

        
        