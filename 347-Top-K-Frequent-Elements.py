class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 1 and k == 1:
            return nums
        hashmap = {}
        trickyList = [[] for x in range(len(nums) + 1)]
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for key, value in hashmap.items():
            trickyList[value].append(key)
        result = []
        for i in range(len(trickyList) - 1, 0, -1):
            if trickyList[i] == []:
                continue
            for num in trickyList[i]:
                if len(result) == k:
                    return result
                result.append(num)
        return result