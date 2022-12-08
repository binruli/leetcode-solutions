class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=heights.copy()
        expected.sort()
        print(expected)
        indices=0
        
        for index in range(len(heights)):
            if heights[index]!=expected[index]:
                indices+=1
                
            
        return indices