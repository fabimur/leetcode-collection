class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            count[s[right]] += 1                 # 1. expandir
            while count[s[right]] > 1:           # 2. contraer mientras sea inválida
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)  # 3. actualizar respuesta
        return max_len