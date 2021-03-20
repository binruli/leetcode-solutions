class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        counterMax = 0
        
        for x in nums:
            if x == 1:
                counter = counter+1
                
            else:
                counterMax = max(counter, counterMax)
                counter = 0
        
        return max(counterMax, counter)