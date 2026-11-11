class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i])) 
        
        cars.sort(key=lambda x:x[0], reverse=True)

        for pos, sp in cars:
            time = (target - pos)/sp
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)
                
        