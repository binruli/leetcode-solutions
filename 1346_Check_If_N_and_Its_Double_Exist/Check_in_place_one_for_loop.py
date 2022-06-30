class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                count +=1
                if count >=2:
                    return True
            elif arr[i]*2 and arr[i]/2 in arr:
                return True
            
        return False