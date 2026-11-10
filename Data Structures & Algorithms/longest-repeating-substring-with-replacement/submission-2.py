class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        6:40
        XYXYXXYY - 2 
        - Maintain a window of i and j
        - Increment j until total distinct values - max(dict.values) = non frequent chars must be less than or equal to K.
        - When the difference above > k, increment i. 
        (0,0) X diff = 0 total = 1
        (0,1) XY diff = 2-1
        (0,2) XYX diff = 3-2 total = 3
        (0,3) xyxy diff = 4-2 total-4
        (0,4) xyxyx diff = 5-3
        (0,5) xyxyxx diff = 6-4
        (0,6) xyxyxxy diff = 7-4 res = 7
        (1,6) yxyxxy diff = 6-3
        (2,6) xyxxy diff = 5-3
        (2,7) xyxxyy diff = 6-3
        (2,8)
        '''
        frequency_map = defaultdict(int)
        i = 0
        j = 0
        N = len(s)
        res = 1
        frequency_map[s[j]]+=1

        while i < N and j < N and i <=j:
            while (j-i+1) - max(frequency_map.values()) <= k:
                res = max(res, j-i+1)
                j+=1
                if j==N:
                    return res
                frequency_map[s[j]]+=1
            frequency_map[s[i]]-=1
            i+=1
        
        return res


            
            

        