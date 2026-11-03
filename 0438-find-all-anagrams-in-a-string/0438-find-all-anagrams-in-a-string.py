class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        window = Counter()
        target = Counter(p)
        result = []
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1

            if right - left + 1 == len(p):
                if window == target:
                    result.append(left)
                window[s[left]] -= 1
                left += 1
                
        return result



        