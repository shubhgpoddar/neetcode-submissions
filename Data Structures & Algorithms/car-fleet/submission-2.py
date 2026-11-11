class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        fleet_time = 0

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i])) 
        
        cars.sort(key=lambda x:x[0], reverse=True)

        for pos, sp in cars:
            time = (target - pos)/sp
            if time > fleet_time:
                fleets+=1
                fleet_time = time

        return fleets
                
        