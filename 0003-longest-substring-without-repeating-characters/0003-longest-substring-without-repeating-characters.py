class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sol = 0
        last = {}

        for right, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1
            last[c] = right
            sol = max(sol, right - left + 1)

        return sol