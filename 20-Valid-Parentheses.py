class Solution(object):
    def isValid(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        stack = []
        m = {'}':'{', ']':'[', ')':'('}
        for c in s:
            if stack and c in m:
                if stack[-1] == m[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack