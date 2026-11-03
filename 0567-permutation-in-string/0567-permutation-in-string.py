from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False


        window = Counter()
        target = Counter(s1)
        target_len = len(s1)
        left = 0
        for right in range(len(s2)):
            window[s2[right]] += 1

            if right - left + 1 > target_len:
                window[s2[left]] -=1
                left += 1
            
            if right - left + 1 == target_len and window == target:
                return True

        return False


        