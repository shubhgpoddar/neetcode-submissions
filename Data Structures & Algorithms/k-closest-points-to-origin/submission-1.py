class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for x,y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, [distance, x, y])
        res = []
        while k!=0:
            point = heapq.heappop(heap)
            print(point)
            res.append([point[1], point[2]])
            k-=1

        return res