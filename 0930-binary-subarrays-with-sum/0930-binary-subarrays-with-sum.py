class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

            def at_most(k: int) -> int:
                if k < 0:
                    return 0
                

                window = 0
                count = 0

                left = 0
                for right in range(len(nums)):
                    window += nums[right]
                    while window > k:
                        window -= nums[left]
                        left += 1
                    
                    if window <= k:
                        count += right - left + 1
                return count

            return at_most(goal) - at_most(goal-1)