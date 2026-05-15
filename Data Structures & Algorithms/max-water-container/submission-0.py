'''
A = W * H
///We start with the widest possible container
///That gives the biggest width, so if we can increase height, we might get a bigger area.
left = 0
right n -1

w = r - l
h = min(l, r)- min height
max_area =  
Which line should I move?”

If I move the taller line, the next container will have:

smaller width

and height still limited by the shorter line (so area can’t increase)

But if I move the shorter line, maybe I find a taller one → possible higher area.
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        max_area = 0
        #As long as the left pointer is before the right pointer, 
        #there’s still a possible container between them.
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

        