class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False


        window_counter = Counter()
        target_counter = Counter(s1)

        left = 0
        for right in range(len(s2)):
            window_counter[s2[right]] += 1

            if right - left + 1 > len(s1):
                window_counter[s2[left]] -= 1
                left += 1

            if window_counter == target_counter:
                return True
        
        return False


        