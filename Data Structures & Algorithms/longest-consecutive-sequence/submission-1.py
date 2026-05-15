'''
set = set([0,3,2,5,4,6,1,1])
0,1,2,3,4,5,6
len = 0
max_len = 0
go thru num nums
if num - 1 not in set- starting of the sequence
    len = 1
    curr = 1
    while num+curr is in set
    len +=1
    curr += 1
    max_len = max(len, maxLen)\
    return maxlen
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_length = 0
        for num in nums:
            if (num - 1) in set_nums:
                continue
            if (num - 1) not in set_nums: #start of a sequence
                len = 1
                curr = 1
                while (num + curr) in set_nums:
                    len += 1
                    curr += 1
            max_length = max(len, max_length)
        return max_length
        

















        # set_num = set(nums)
        # max_len = 0

        # for num in nums:
        #     if num - 1 not in set_num:
        #         length = 1
        #         curr = 1 #used to move forward through the consecutive numbers
        #         while num + curr in set_num:
        #             length += 1
        #             curr += 1
        #         max_len = max(length, max_len) #Every time you finish counting a streak
        # return max_len
