class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for c in s.lower():
            count_s[c] += 1
        for c in t.lower():
            count_t[c] += 1
        return count_s == count_t

