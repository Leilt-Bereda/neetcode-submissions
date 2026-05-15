'''
1,2,3,1  k = 3
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                diff = abs(i-j)
                if nums[i] == nums[j] and diff <= k:
                    return True
        return False

