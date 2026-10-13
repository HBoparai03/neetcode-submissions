class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashset:
                return [hashset[difference], i]
            hashset[nums[i]] = i