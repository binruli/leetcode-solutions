class Solution:
    def removeElement(self, nums: int, val: int) -> int:
        for numbers in range(len(nums)):
            if val not in nums:
                break
            if len(nums) == 0:
                return 0
            else:
                nums.remove(val)
            
        print(len(nums))
        print ("nums = ",nums)