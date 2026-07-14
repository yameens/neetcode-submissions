class MinStack:

    def __init__(self):
        self.minimum = [float("infinity")]
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum[-1]: ## you capture every minimum instance, in the case that all mins are popped you do not wish to access inf
            self.minimum.append(val)

    def pop(self) -> None:
        if self.minimum[-1] == self.stack[-1]:
            del self.minimum[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        
