class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        baskets = Counter()
        result = 0
        
        left = 0
        for right in range(len(fruits)):
            baskets[fruits[right]] += 1

            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1
            
            result = max(result, baskets.total())



        return result
        
        