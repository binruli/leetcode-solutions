class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        newSet=set(nums)
        disNumbers=[]
        maxNumber=len(nums)

        for number in range(1, maxNumber+1):
            if number not in newSet:
                disNumbers.append(number)
            
        return disNumbers