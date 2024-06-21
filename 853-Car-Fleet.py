class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(position)
        if n == 1:
            return 1
        
        stack = []
        pairs = sorted(zip(position, speed), reverse=True)
        
        for p, s in pairs:
            time = float((target - p)) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        
        return len(stack)
