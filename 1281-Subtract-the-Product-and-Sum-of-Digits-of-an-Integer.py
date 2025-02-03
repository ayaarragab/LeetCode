class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_n = 0
        product_n = 1
        while n > 0:
            sum_n += n % 10
            product_n *= n % 10
            n //= 10
        return product_n - sum_n