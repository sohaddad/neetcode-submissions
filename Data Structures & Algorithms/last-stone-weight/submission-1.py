class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            max1 = -heapq.heappop(max_heap)
            max2 = -heapq.heappop(max_heap)

            difference = max1 - max2
            if difference > 0:
                heapq.heappush(max_heap, -difference)
            
        max_heap.append(0)
        return abs(max_heap[0])