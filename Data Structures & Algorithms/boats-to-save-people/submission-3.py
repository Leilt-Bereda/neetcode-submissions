'''
1,2,4,5
 1 + 5= 6 -> 1
 2+4= 6 -> 1
 b = 2

 1,2,2,3,3  l = 3
 1+3= 4 b= 1
 1+3 = 4 b=1
 1+2=3 b = 1
 2 b = 1
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l = 0 
        r = n - 1
        boat = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                boat += 1
            elif people[l] + people[r] > limit:
                boat += 1
                r -= 1
                continue
            l += 1
            r -= 1
        return boat
            