class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1 = sorted(nums1)
        arr2 = sorted(nums2)
        i , j = 0, 0
        output = []
        while i<len(arr1) and j< len(arr2):
            if arr1[i] > arr2[j]:
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else:
                output.append(arr1[i])
                i += 1
                j += 1
        return output
                