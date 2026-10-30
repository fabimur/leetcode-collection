class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        last = {}
        sol = 0

        for right in range(len(s)):
            if s[right] in last and left <= last[s[right]]:
                left = last[s[right]] + 1
            last[s[right]] = right
            sol = max(sol, right - left + 1)

        return sol