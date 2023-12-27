class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        strVal = ""
        len1, len2 = len(word1), len(word2)
        minLen = min(len1, len2)

        for i in range(minLen):
            strVal += word1[i] + word2[i]

        strVal += word1[minLen:] + word2[minLen:]

        return strVal