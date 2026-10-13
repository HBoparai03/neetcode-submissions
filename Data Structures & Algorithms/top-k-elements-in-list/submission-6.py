class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        result = []
        highest = 0
        most = None
        count = 0
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        while count < k:
            for num, frequency in seen.items():
                if frequency > highest:
                    most = num
                    highest = frequency
            result.append(most)
            count += 1
            highest = 0
            seen.pop(most)
        return result