class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1 or s[0] in "})]":
            return False
        stack = []
        hashMap = {"]":"[", "}":"{", ")":"("}
        for i, l in enumerate(s):
            if l in "{([":
                stack.append(l)
                continue
            else:
                t = hashMap[l]
                if stack and stack[-1] == t:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
