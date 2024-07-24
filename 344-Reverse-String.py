class Solution(object):
    def reverseString(self, s):
        \\\
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        \\\
        i = 0
        n = len(s)
        k = n - 1
        while i < k:
            temp = s[i]
            s[i] = s[k]
            s[k] = temp
            i += 1
            k -= 1
        return s