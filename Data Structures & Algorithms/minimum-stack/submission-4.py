class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minimum = float("inf")

        for s in self.stack: 
            if minimum > s: 
                minimum = s

        return minimum
