'''
defaultdict= key is the sorted string and value is a list of strings that match the sorted string
'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        res = []
        for val in groups.values():
            res.append(val)
        return res
