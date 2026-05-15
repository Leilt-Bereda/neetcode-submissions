class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            n = 1
            for j in range(len(nums)):
                if j != i:
                    n *= nums[j]
            output.append(n)
        return output
       
