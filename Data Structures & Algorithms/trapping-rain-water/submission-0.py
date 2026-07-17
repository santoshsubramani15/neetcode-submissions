class Solution:
    def trap(self, height: List[int]) -> int:
        h=len(height)
        if h==0:
            return 0

        leftMax = [0]*h
        rightMax = [0]*h

        leftMax[0] = height[0]
        for i in range(1, h):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[h - 1] = height[h - 1]
        for i in range(h - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        res = 0
        for i in range(h):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res