class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, height in enumerate(heights):
            start = i 
            if stack: 
                while stack and stack[-1][0] > height: 
                    stackHeight, index = stack.pop()
                    maxArea = max(maxArea, stackHeight * (i - index)) ## calculates the area leftward
                    start = index
            stack.append((height, start)) ## what can the smaller bar extend to at the left ? 

        finalLength = len(heights)

        for bar in stack: 
            stackHeight, index = bar[0], bar[1]
            maxArea = max(maxArea, stackHeight * (finalLength - index)) ## nothing smaller on the right. then we can extend all the way over
        
        return maxArea
        