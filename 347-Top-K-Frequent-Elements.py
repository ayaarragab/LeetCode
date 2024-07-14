class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        listOflists = [[] for _ in range(len(nums) + 1)]
        l = []
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        for key, v in d.items():
            listOflists[v].append(key)
        for i in range(len(listOflists) - 1, 0, -1):
            for num in listOflists[i]:
                if len(l) == k:
                    break
                l.append(num)
        return l