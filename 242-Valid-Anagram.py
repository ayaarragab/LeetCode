class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if n != len(t):
            return False 
        set_s = set(s)
        set_t = set(t)
        if set_s != set_t:
            return False
        for char in set_t:
            if s.count(char) != t.count(char):
                return False
        return True