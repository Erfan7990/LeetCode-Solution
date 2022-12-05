class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            value = str(i)
            if len(value)%2 == 0:
                cnt += 1;
        return cnt