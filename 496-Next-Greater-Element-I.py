class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out = []
        l = len(nums2)
        for num in nums1:
            found = False
            idx = nums2.index(num)
            if idx < l:
                for i in range(idx + 1, l):
                    if nums2[i] > num:
                        out.append(nums2[i])
                        found = True
                        break
            if not found:
                    out.append(-1)
        return out