class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1
        sum_ = 0
        p_n = n
        while p_n:
            d = p_n % 10
            product *= d
            sum_ += d
            p_n //= 10
        return product - sum_
