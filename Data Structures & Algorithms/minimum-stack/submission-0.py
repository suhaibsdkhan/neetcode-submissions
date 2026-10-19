class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        #if minStack exists then push the largest either new added val or existing
        if self.minStack:
            self.minStack.append(min(self.minStack[-1],val))
        else: #if minStack does not exist then add the new value as minStacks value 
            self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
