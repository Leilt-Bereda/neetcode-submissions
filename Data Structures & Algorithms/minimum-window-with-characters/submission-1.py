from collections import Counter
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = defaultdict(int)
        l = 0
        have = 0
        need = len(count_t)
        resLen = float('inf')
        res = ""
        for r in range(len(s)):
            count_s[s[r]] += 1
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]] :
                have += 1
            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                count_s[s[l]] -= 1

                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        return res
                    

