class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        newArray = []
        for i1 in range(len(nums1)):
            if i1 >= m:
                break
            else:
                newArray.append(nums1[i1])
            
        
        
        for i2 in range(len(nums2)):
            newArray.append(nums2[i2])
        
        
        newArray = sorted(newArray)
        
        
        
        for i3 in range(len(nums1)):
            nums1[i3] = newArray[i3]