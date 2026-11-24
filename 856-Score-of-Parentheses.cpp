class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = [0]
        for c in s:
            if c == "(":
                stk.append(0)
            else:
                value = max(2 * stk.pop(), 1)
                stk[-1] += value
        return stk.pop()
