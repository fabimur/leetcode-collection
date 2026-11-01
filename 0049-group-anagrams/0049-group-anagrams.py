class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())