class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredNums = []
        for numbers in nums:
            numbers = numbers*numbers
            squaredNums.append(numbers)
        return sorted(squaredNums)