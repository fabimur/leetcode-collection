class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(word))
            anagram_dict[sorted_word].append(word)

        return list(anagram_dict.values())