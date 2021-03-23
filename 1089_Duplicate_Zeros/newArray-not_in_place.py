class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        newArray = []
        for numbers in arr:
            if numbers == 0:
                newArray.extend((0,0))
            else:
                newArray.append(numbers)
        for i in range(len(arr)):
            arr[i] = newArray[i]