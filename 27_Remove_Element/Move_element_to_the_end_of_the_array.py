class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        for numbers in range(len(nums)):
            i = nums[numbers]
            if nums[numbers] == val:
                nums.pop(numbers)
                nums.append(i)
                count = count +1
                
        print(count)