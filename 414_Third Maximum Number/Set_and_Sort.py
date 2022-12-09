class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxNum=0
        secondMaxNum=0
        thirdMaxNum=0
        
        arrSet=set(nums)
        newArr=list(arrSet)
        newArr.sort()
        print(newArr)
        for index in range(len(newArr)):
            if len(newArr)<3:
                thirdMaxNum=max(newArr)
        
        endPoint=len(newArr)-1
        for endPoint in range(len(newArr)):
            if endPoint==len(newArr)-3:
                thirdMaxNum=newArr[endPoint]
                
            
        return thirdMaxNum