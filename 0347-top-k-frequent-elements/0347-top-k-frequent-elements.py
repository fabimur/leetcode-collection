class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

 
        sortedNum = sorted(count.keys(), key = lambda x: -count[x])

        return sortedNum[:k]