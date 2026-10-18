class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        l = len(heights)
        start = 0
        end = l - 1
        for i in range(l):
           height = min(heights[start],heights[end])
           width = end - start
           a = width * height
           if a > max_a:
            max_a = a
           if heights[start] < heights[end]:
            start += 1
           else:
            end -= 1
        return max_a
           
