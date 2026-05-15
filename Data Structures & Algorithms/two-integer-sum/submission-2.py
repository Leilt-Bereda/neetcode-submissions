'''
i == j 
nums = [3,4,5,6], target = 7
hashmap to store each numbet with its index
find diff - target - num
check if diff in our hashmap
add the num to our hashmap
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i