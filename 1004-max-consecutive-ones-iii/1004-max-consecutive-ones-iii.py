class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        flips = 0
        max_window = 0

        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                flips += 1

            while flips > k:
                if nums[left] == 0:
                    flips -= 1
                left += 1
            
            max_window = max(max_window, right-left + 1)

        return max_window
        