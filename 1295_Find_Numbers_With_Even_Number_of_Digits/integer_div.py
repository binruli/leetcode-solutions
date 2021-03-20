class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for numbers in nums:
            counter_div = 0
            while numbers != 0:
                numbers = numbers//10
                counter_div = counter_div + 1
            if counter_div %2 == 0 and counter_div !=0:
                counter = counter + 1
                
        return counter