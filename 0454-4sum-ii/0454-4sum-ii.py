from collections import Counter

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        sums = Counter(a + b for a in nums1 for b in nums2)

        res = 0
        for c in nums3:
            for d in nums4:
                res += sums[-(c + d)]

        return res