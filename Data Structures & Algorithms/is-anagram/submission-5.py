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
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        count_t = Counter(t)

        return count_s == count_t
        