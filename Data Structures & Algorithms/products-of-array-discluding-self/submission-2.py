class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [] 
        left = []
        result = []
        product = 1

        for num in nums:
            left.append(product)
            product = product * num
        
        product = 1
        for num in reversed(nums):
            right.append(product)
            product = product * num
        right.reverse()

        for i in range(len(nums)):
            result.append(left[i]*right[i])
        return result

        