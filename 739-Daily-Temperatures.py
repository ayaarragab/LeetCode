class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        output = [0] * len(temperatures)
        stack = []
        for i, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                e = stack.pop()
                output[e] = abs(e - i)
            stack.append(i)
        return output