class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for j in range(1, len(arr)):
            for i in range(len(arr)):
                if i != j and (arr[i] == 2*arr[j] or arr[i] == arr[j]/2) :
                    return True