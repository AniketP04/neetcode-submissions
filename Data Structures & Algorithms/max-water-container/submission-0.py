class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        res = 0

        while left < right:
            width = right - left
            current_height = min(heights[right], heights[left])
            current_area = current_height * width

            res = max(current_area, res)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res