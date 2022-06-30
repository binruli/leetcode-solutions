class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        myset = set()
        count = 0
        for i in arr:
            if i == 0:
                count +=1
                if count >=2:
                    return True
            else:
                myset.add(i)
                
        for j in myset:
            if j*2 in myset:
                return True
            
        return False