class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        n = len(height)

        for i in range(len(height)):
            leftMax = 0
            rightMax = 0

            for l in range(i + 1):
                leftMax = max(leftMax, height[l])

            for r in range(i, n):
                rightMax = max(rightMax, height[r])
            
            res += min(leftMax, rightMax) - height[i]
        return res        