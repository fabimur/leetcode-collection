class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        best = 0
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1

            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best