class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        k = len(numbers) - 1

        while i < k:
            s = numbers[i] + numbers[k]

            if s == target:
                return [i + 1, k + 1] 
            elif s < target:
                i += 1
            else:
                k -= 1
