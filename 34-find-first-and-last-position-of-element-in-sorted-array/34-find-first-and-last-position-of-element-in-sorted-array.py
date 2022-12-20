class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = self.searchIndex(nums, target, True)
        end = self.searchIndex(nums, target, False)
        
        return [start, end] 
    
    def searchIndex(self, nums, target, leftbias):
        start,end = 0,len(nums)-1
        ans=-1
        while start<=end:
            
            mid= (start+end)//2
            if target>nums[mid]:
                start =mid+1
            elif target<nums[mid]:
                end =mid-1 
            else:
                ans =mid
                if leftbias:
                    end=mid-1 
                else:
                    start=mid+1
        return ans
                    