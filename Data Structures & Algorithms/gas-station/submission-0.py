'''
gas = [1,2,3,4]
cost = [2,2,4,1]
sum(gas) < cost - return -1
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n): #chooses the starting point
            tank = 0
            completed = True

            for i in range(n): #see if we can complete a full trip from that point
                j = (start + i) % n #need to start checking from the chosen start position and loop around
                tank += gas[j] - cost[j]
                if tank < 0:
                    completed = False
                    break
            if completed:
                return start
        return -1
                
            