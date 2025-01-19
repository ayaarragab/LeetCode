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
                self.min_states.append(val)
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        element = self.stack.pop()
        if element == self.min_states[-1] and element not in self.stack:
            self.min_states.pop()
            self.min = None if not self.min_states else self.min_states[-1]
        return element

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