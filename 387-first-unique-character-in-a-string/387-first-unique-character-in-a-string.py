class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for k, v in enumerate(s):
            if count[v] is 1:
                return k
        return -1