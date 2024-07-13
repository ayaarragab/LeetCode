class Solution(object):
    def containsDuplicate(self, nums):
        \\\
        :type nums: List[int]
        :rtype: bool
        \\\
        f = set()
        for num in nums:
            if num in f:
                return True
            else:
                f.add(num)
        return False