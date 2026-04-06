class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')
        

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val - self.mini)
            if val < self.mini:
                self.mini = val
        else:
            self.mini = val
            self.stack.append(0)
        

    def pop(self) -> None:
        x = self.stack.pop()

        if x < 0:
            self.mini = self.mini - x
        

    def top(self) -> int:
        x = self.stack[-1]

        if x > 0:
            return self.mini + x
        else:
            return self.mini
        

    def getMin(self) -> int:
        return self.mini
        
