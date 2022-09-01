class MinStack(object):

    def __init__(self):
        self.data = []
        self.smalls = []
        self.topVal = -1
        

    def push(self, val):
        self.data.append(val)
        self.topVal += 1
        if (len(self.smalls) == 0) or (val < self.smalls[-1]):
            self.smalls.append(val)
        else:
            self.smalls.append(self.smalls[-1])

    def pop(self):
        if self.topVal == -1:
            return -1
        self.topVal -= 1
        self.smalls.pop()
        return self.data.pop()
        

    def top(self):
        return self.data[-1]
        

    def getMin(self):
        return self.smalls[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()