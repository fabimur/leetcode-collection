class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sol = 0
        seen = {}

        for right in range(len(s)):
            char = s[right]
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            sol = max(sol, right - left + 1)

        return sol
