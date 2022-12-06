class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr=[]
        for index in range(len(nums)):
            if nums[index]%2 == 0:
                arr.insert(0,nums[index])
            else:
                arr.insert(len(nums),nums[index])
                
        return arr