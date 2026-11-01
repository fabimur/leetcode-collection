class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        max_sequence = 0

        for n in seen:
            if n - 1 not in seen:
                current_num = n
                current_sequence = 1
                while current_num + 1 in seen:
                    current_num += 1
                    current_sequence += 1
                max_sequence = max(max_sequence, current_sequence)

        return max_sequence