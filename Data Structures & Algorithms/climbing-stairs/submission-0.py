'''
1 or 2
basecase- i == n and i > n
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)
        