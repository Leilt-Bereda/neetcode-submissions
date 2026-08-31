class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a)) 
                #int() converts to an integer and rounds it toward 0
            elif c == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            else:
                stack.append(int(c))
        return stack[-1]