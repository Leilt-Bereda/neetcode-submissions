class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        left_max = height[l]
        right_max = height[r]
        water_trapped = 0
        while l < r:
            if height[l] < height[r]:
                water_trapped += left_max - height[l]
                l += 1
                left_max = max(left_max, height[l])
            else:
                water_trapped += right_max - height[r]
                r -= 1
                right_max = max(right_max, height[r])
        return water_trapped 