class CustomStack(object):

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.top = -1
        self.data = []
        

    def push(self, x):
        if self.top+1 < self.maxSize:
            self.data.append(x)
            self.top += 1

    def pop(self):
        if self.top == -1:
            return -1
        self.top -= 1
        return self.data.pop()
        

    def increment(self, k, val):
        if k > self.top+1:
            k = self.top+1
        for i in range(k-1, -1, -1):
            self.data[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)