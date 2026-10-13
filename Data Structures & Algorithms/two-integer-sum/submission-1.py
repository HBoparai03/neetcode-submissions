class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in hashset:
                return [hashset[n], i]
            hashset[nums[i]] = i
        return[]