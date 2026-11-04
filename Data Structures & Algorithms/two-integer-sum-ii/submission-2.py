class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        11/3 5:28
        Conditions:
        a) i + j = target and i < j.
        b) i should not be equal to j

        Algorithm:
        2 pointer approach. 
        if sum > target: move j to left
        if sum < target: move i to right
        else: return i+1 , j+1

        Output: 1- indexed indixes [i, j]

        O(1) space mandatory
        '''
        N = len(numbers)
        i = 0
        j = N-1

        while(i < N and j >=0 and i < j):
            total = numbers[i] + numbers[j]
            if total > target:
                j-=1
            elif total < target:
                i+=1
            else:
                return [i+1, j+1]
        return []
        
        