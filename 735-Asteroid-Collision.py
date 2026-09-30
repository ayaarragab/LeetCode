class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stk = []
        for n in asteroids:
            while stk and n < 0 < stk[-1]:
                if stk[-1] < -n:
                    stk.pop()
                    continue
                elif stk[-1] == -n:
                    stk.pop()
                break
            else:
                stk.append(n)
        return stk