'''
all possible combinations of elements that can be formed from the array
no duplicates
[], [1] [], [1,2] [1]
i >= len(nums)
res = []- stores all subsets(the final result)
subset = []- the list of all subsets we have so far
start wiht an empty {}- no decision made
include- append
not include- pop
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []

        def backtrack(i):
            #base case
            if i >= n:
                res.append(subset.copy()) # we wanna save a snapshot of the current subset
                return
            # include
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            # not include
            backtrack(i + 1)
        backtrack(0)
        return res