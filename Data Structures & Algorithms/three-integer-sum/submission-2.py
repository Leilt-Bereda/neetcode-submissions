'''
1. sort nums
2. choose 1 fixed number in every iteration, until we have 2 nums remaining in our nums
- when i > 0, compare with i-1. if i == i-1 then skip
3. find the remaining pair using the two-pointers technique
- if we have a valid triplet, add it our result and move both pointers inward
    -After finding a valid triplet (skip duplicate left and right values)
4. store our result in a set, since it wont allow duplicates
5. convert the set to a list and return

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum < 0:
                    l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    
        return res
                