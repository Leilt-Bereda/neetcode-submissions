class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # check if we have a cycle
        # slow pointer moves one step
        # fast pointer moves 2 times faster than the slow
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # determine the entry of the cycle, which is the duplicate
        # reset the slow pointer and move both pointers with the same speed
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
        