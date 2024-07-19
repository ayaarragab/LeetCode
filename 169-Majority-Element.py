class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_f = len(nums) // 2
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for k,v in d.items():
            if v > n_f:
                return k