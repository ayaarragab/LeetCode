class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        occurances = 0
        length = len(nums)
        si = []
        for num in nums:
            if num == val:
                occurances += 1
        k = length - occurances # k = 1, length = 3
        i = 0
        for i in range(0, k): # 1st: i = 0, nums = [2, 2, 3]
            if nums[i] == val: 
                if not si:
                    si.append(k)
                s = si.pop()
                for j in range(s, length):
                    if nums[j] != val:
                        temp = nums[j]
                        nums[j] = val
                        nums[i] = temp
                        if j + 1 < length:
                            si.append(j + 1)
                        break
        return k