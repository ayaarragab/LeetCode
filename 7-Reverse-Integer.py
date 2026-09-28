class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x % 10 == x:
            return x
        stack = []
        is_negative = x < 0
        x = abs(x)
        rev_x = 0
        multip = 1
        while x:
            d = x % 10
            x //= 10
            stack.append(d)
        while stack:
            rev_x += stack.pop() * multip
            multip *= 10
        rev_x = - rev_x if is_negative else rev_x
        if rev_x < -2**31 or rev_x > 2**31 - 1:
            return 0
        return rev_x