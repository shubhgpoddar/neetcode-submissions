class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = [(40,5), (28,6)]
        # res = [1, 4, 1, 2, 1, 0, 0]
        n = len(temperatures)
        res = [0]*n

        stack = []

        for i in range(n):
            temp = temperatures[i]
            while stack and temp > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temp, i))
        return res


        