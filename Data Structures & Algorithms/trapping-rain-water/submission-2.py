class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        leftmax = height[left]
        rightmax = height[right]
        result  = 0
        while left < right:
            if leftmax < rightmax:
                left += 1
                if leftmax < height[left]:
                    leftmax = height[left]
                else:
                    result += max(0, min(leftmax, rightmax) - height[left])
            else:
                right -= 1
                if rightmax < height[right]:
                    rightmax = height[right]
                else:
                    result += max(0, min(leftmax, rightmax) - height[right])
        return result

        