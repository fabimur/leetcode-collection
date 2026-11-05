class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atMost(k: int) -> int:
            if k < 0:
                return 0

            count = 0

            window = 0

            left = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    window += 1

                while window > k:
                    if nums[left] % 2 == 1:
                        window -= 1
                    left += 1

                count += right - left + 1

            return count

        return atMost(k) - atMost(k-1)