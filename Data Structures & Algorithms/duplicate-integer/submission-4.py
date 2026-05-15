'''
create an empty set
go thru num in nums:
if num in set:
    return true
else:
    add to our set
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False