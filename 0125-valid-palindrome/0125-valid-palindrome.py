class Solution(object):
    def isPalindrome(self, s):
        parsed = []
        for c in s:
            if c.isalnum():
                parsed.append(c.lower())

        return parsed == parsed[::-1]
