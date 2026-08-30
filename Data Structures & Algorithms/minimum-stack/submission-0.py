class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        num = self.stack.pop()
        if self.minStack and num == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        
