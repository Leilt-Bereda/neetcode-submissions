'''
sort the array so that we can see who are the heavies and lightest
using the 2 pointers technique
l- keeps track of the lightest person
r- keeps track of the heaviest person
iterate thru the array(while l <= r)
if l + r <= limit:
    append(l,r)
    increment both pointers
elif:
    append(r)
    increment r
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        boats = []
        while l <= r:
            if people[l] + people[r] <= limit:
                boats.append([people[l], people[r]])
                l += 1
                r -= 1
            else:
                boats.append(people[r])
                r -= 1
        return len(boats)