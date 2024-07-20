class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for _ in range(n)]
        prefix, postfix = 1, 1
        for i in range(0, n):
            res[i] = prefix
            prefix *= nums[i]
        for k in range(n - 1, -1 , -1):
            res[k] *= postfix
            postfix *= nums[k]
        return res