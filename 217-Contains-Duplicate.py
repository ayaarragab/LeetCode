class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_set = {}
        for num in nums:
            if num in hash_set:
                return True
            hash_set[num] = 1
        return False
