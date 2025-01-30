class Solution(object):
    def isPowerOfTwo(self, n):
        \\\
        :type n: int
        :rtype: bool
        \\\
        if n <= 0:
            return False  # Negative numbers and zero are NOT powers of two

        binary = bin(n)[2:]  # Convert to binary without the '0b' prefix
        return binary.count('1') == 1  # Power of two should have exactly one '1'