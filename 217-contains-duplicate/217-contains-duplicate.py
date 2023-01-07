class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hasSet = set()
        for i in nums:
            if i in hasSet:
                return True
            else:
                hasSet.add(i)
            