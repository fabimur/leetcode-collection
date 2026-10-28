class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        numbers = list(count)
        numbers.sort(key = lambda x: numbers[x][1])

        return numbers[:k]