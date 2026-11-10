class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        6:40
        XYXYXXYY - 2 
        - Maintain a window of i and j
        - Increment j until total distinct values - max(dict.values) = non frequent chars must be less than or equal to K.
        - When the difference above > k, increment i. 
        '''
        frequency_map = defaultdict(int)
        i = 0
        j = 0
        N = len(s)
        maxF = 0
        res = 0

        while i < N and j < N and i <=j:
            frequency_map[s[j]]+=1
            maxF = max(maxF, frequency_map[s[j]])
            if (j-i+1) - maxF <= k:
                res = max(res, j-i+1)
            else:  
                frequency_map[s[i]]-=1
                i+=1
            j+=1
        
        return res


            
            

        