class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_ = sum(nums)
        sum_d = 0
        for num in nums:
            while num > 0:
                sum_d += num % 10
                num //= 10
        return abs(sum_ - sum_d)