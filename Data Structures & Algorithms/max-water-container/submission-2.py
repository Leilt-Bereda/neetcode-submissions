'''
h w
   l r
[1,7,2,5,4,7,3,6]
w = l - r = 7
h = 1
a = 7

w = 6 h = 6 a = 36
w = 5 h = 3 a = 15
w = 4 h = 7 a = 28
w = 3 h = 4 a = 12
w = 2 h = 5 a = 10
w = 1 h = 2 a = 2

'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        max_area = 0
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            area = w * h
            print(area)
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area