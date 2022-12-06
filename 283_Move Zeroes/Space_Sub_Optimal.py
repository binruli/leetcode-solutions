class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        deleIndex = len(nums)
        print(deleIndex)
        count = 0
        for index in range(len(nums)):
            if nums[index]==0:
                count=count+1
            index=index+1
        print(count)
            
        for index in range(len(nums)):
            if nums[index]!=0:
                nums.append(nums[index])
        
        i=0
        while i < count:
            nums.append(0)
            i = i +1
        
        del nums[0:deleIndex]
        