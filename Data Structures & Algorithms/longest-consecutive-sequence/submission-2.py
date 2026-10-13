class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        check = set(nums)

        for i in range(len(nums)):
            if (nums[i] - 1) not in check:
                length = 1
                while (nums[i] + length) in check:
                    length +=1
                ans = max(ans, length)
        return ans
                
