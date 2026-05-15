'''
start with an open bracket
hashmap = }-{ ]-[ )-(
go thru c in s
append open bracket to my stack
if c in hashmap: - if its a closed
    if stack[-1] == c:
        pop
    else return false
else append it to our stack
true if stack
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False