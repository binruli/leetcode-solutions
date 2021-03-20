class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for numbers in nums:
            converted_num = str(numbers)
            if len(converted_num) %2 == 0:
                counter = counter + 1
                
        return counter