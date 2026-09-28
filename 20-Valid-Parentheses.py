class Solution(object):
    def is_right_para(self, c1, c2):
        comb = c1 + c2
        return comb == "()" or comb == "{}" or comb == "[]"


    def isValid(self, s):
        if not s:
            return True
        stk = []
        for c in s:
            if c in "([{":
                stk.append(c)
            elif len(stk) and self.is_right_para(stk[-1], c):
                stk.pop()
            else:
                return False
        return len(stk) == 0