import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-x for x in nums]
        heapq.heapify(nums)
        res = None
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res