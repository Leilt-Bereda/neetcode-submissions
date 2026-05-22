from collections import defaultdict
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        sub_count = defaultdict(int)
        k = len(s1)
        if len(s2) < k:
            return False
        for i in range(k):
            sub_count[s2[i]] += 1
        for i in range(k, len(s2)):
            if sub_count == s1_count:
                return True
            sub_count[s2[i]] += 1
            sub_count[s2[i-k]] -= 1
            if sub_count[s2[i-k]] == 0:
                del sub_count[s2[i-k]]
        return sub_count == s1_count
                
        
                
        
            
