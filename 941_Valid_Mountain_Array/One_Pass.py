class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        index = 0
        arrLength = len(arr)
        if arrLength < 3:
            return False
        while index+1 < arrLength and arr[index] < arr[index+1]:
            index += 1
        if index == 0 or index == arrLength-1:
            return False
        while index+1 < arrLength and arr[index] > arr[index+1]:
            index +=1
            
        return index == arrLength-1