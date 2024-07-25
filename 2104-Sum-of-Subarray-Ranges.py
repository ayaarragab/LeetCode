class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(nums)
        sum_ = 0
        range_ = 0
        j = 0
        while i < n:
            j = i + 1
            mx = nums[i]
            mn = nums[i]
            while j < n:
                mx = max(mx, nums[j])
                mn = min(mn, nums[j])
                range_ = mx - mn
                sum_ += range_
                j += 1
            i += 1
        return sum_
