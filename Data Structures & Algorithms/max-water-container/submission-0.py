class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #this one is width times height in which the width 
        #wait this is a pointers question
        l = 0
        r = len(heights) - 1
        maximumarea = 0

        while l < r:
            width = r - l
            h = min(heights[l], heights[r])
            area = width * h
            maximumarea = max(maximumarea, area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maximumarea
