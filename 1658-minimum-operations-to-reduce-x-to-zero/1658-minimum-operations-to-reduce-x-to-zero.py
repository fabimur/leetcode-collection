class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1

        window = 0
        max_window = -1

        left = 0
        for right in range(len(nums)):
            window += nums[right]
            while window > target:
                window -= nums[left]
                left += 1
            
            if window == target:
                max_window = max(max_window, right-left+1)

        return len(nums) - max_window if max_window != -1 else -1

            
            
