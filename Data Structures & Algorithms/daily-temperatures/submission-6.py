class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        11/4 6:24
        '''
        N = len(temperatures)
        res = [0]*N
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, i = stack.pop(-1)
                res[i] = index - i
            stack.append((temp, index))
        return res



        