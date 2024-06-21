class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                sVal, sIdx = stack.pop()
                result[sIdx] = i - sIdx
            stack.append([t, i])
        return result