class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum[-1]: 
            self.minimum.append(val)
        

    def pop(self) -> None:
        if self.stack[-1] == self.minimum[-1]:
            del self.minimum[-1]
        del self.stack[-1]
        

        ## .remove() removes based on value NOT index ! 
        ## you need to use DELETE

        ## double stack allows you to keep the min organized ! 

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        ## o(n)
