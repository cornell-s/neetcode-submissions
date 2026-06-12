class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0
        l = 0
        r = len(heights) - 1 

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            area = height * width

            total = max(total, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1 

        return total