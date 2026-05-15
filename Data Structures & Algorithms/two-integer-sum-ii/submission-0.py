'''
input- sorted arrat
output- indeces of the two numbers
[2,7,11,15] target= 9
diff= target - num= 7
if diff not in hashmap:
    add to hashmap
if diff in hashmap:
    return 

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in seen:
                return [seen[diff] + 1, i + 1 ]
            seen[numbers[i]] = i 