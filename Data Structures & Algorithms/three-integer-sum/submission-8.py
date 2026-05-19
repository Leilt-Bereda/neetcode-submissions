class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        target = 0
        result = []
        for i in range(n - 2):
            # handle duplicates at the beginning
            # whenever i > 0 compare it to previous if we have duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                curr = nums[l] + nums[r]
                if nums[i] + curr < target:
                    l += 1
                elif nums[i] + curr > target:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    # skip duplicate 
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    # at the end of this while loop our pointers are pointing to the last 
                    # occurence of the duplicate and we still wanna skip that so we increment the pointers

                    l += 1
                    r -= 1

        return result

                