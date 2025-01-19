class MinStack(object):
    def __init__(self):
        self.min = None
        self.min_states = []
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.min = val
            self.min_states.append(val)
        elif val < self.min:
            self.min = val
        self.stack.append(val)
        self.min_states.append(min(val, self.min_states[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.min_states.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return None if not self.min_states else self.min_states[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()