class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in '{([':
                stack.append(c)
            else:
                if stack and stack[-1] == '{' and c == '}':
                    stack.pop()
                elif stack and stack[-1] == '(' and c == ')':
                    stack.pop()
                elif stack and stack[-1] == '[' and c == ']':
                    stack.pop()
                else:
                    return False
        return not stack