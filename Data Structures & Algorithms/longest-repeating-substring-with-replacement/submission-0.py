'''
"AAABABB"  k = 1
hashmap- count the frquency of the characters within the current window
invalid = size - mostFreq > k
''' 
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq = 0
        res = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            freq = count.values()
            maxFreq = max(freq)
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            




