class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for num in nums]
        pre = 1
        post = 1
        n = len(nums)
        for i in range(0, n):
            if i == 0:
                res[0] = 1
                continue
            pre *= nums[i - 1]
            res[i] = pre
        for k in range(n - 1, -1, -1):
            res[k] *= post
            post *= nums[k]
        return res