class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        sortedNums = sorted(count.keys(), key = lambda x: -count[x])

        return sortedNums[:k]