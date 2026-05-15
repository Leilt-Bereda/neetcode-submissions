'''
same number of characters
len(s) == len(t)
same frequency of those characters
s = "racecar", t = "carrace"
r:2  c: 2
a:2  a:2
c:2  r:2
e:1  e:1

'''
from collections import Counter
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = defaultdict(int)
        for c in s:
            count_s[c] += 1
        count_t = Counter(t)

        return count_s == count_t
        