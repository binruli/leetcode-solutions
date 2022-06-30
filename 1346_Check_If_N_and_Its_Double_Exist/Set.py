class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        myset = set()
        count = 0
        for i in arr:
            if i*2 in myset or i/2 in myset:
                return True
            myset.add(i)
        return False