'''
it should start with an open bracket
string = "" return true
When you see a closing bracket,
does it match the latest opening bracket (the top of the stack)?

That means:
"([{}])"
stack = ([{
check if they are the same type
closeToOpen = )(, }{, ][
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: 
                    # { == {?
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

