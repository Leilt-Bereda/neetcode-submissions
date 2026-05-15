from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = defaultdict(int)
        count_s2 = defaultdict(int)
        k = len(s1)
        if len(s2) < len(s1):
            return False
        for i in range(k):
            count_s1[s1[i]] += 1
        for i in range(k):
            count_s2[s2[i]] += 1
        for i in range(k, len(s2)):
            if count_s2 == count_s1:
                return True
            else:
                count_s2[s2[i]] += 1
                count_s2[s2[i - k]] -= 1
                if count_s2[s2[i - k]] == 0:
                    del count_s2[s2[i - k]]
        return count_s1 == count_s2




       
        
