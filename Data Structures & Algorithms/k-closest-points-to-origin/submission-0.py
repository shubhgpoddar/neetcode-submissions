class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []
        for x,y in points:
            distance = math.sqrt(x**2 + y**2)
            res.append([distance, x, y])
        print(res)
        res.sort(key=lambda x:x[0])
        print(res)

        output = []
        for i in range(k):
            output.append([res[i][1], res[i][2]])
        return output


            
        