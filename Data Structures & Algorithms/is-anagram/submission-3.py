from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        # for c in s:
        #     if c in count_s:
        #         count_s[c] += 1
        #     count_s[c] = 1
        count_t = Counter(t)
        return count_s == count_t