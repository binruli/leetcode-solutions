class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        newSet={}
        disNumbers=[]
        for number in nums:
            newSet[number]=1
        
        for index in range(1,len(nums)+1):
            if index not in newSet:
                disNumbers.append(index)
        return disNumbers