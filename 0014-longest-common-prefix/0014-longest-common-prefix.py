class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = strs[0]

        for i, c in enumerate(first):
            for word in strs[1:]:
                if i >= len(word) or word[i] != c:
                    return first[:i]

        return first