class Solution(object):
    def isPalindrome(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        clean_text = clean_text.lower()
        n = len(clean_text)
        print(clean_text)
        if (clean_text[:n // 2] == clean_text[-1:n // 2:-1]) or (clean_text[:n / 2] == clean_text[-1:(n - 1) // 2:-1]):
            return True
        else:
            return False