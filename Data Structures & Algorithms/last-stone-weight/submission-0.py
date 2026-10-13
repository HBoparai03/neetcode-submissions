class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            largest = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if largest == second:
                continue
            else:
                newstone = largest - second
                heapq.heappush(heap, -newstone)

        return -heap[0] if heap else 0

        
        