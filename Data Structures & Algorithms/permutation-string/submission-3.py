class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        11/3 8:39
        brute force:
        1) sort s1. 
        2) For each substring in s2 [0:s1+1]. if sorted is same then return True. If not move left and right pointers by 1 until we find a match
        s1 = a and s2 = ab
        '''
        s1 = sorted(s1)
        N1 = len(s1)

        i = 0
        N2 = len(s2)
        j = i + N1 - 1

        while(i < N2 and j < N2 and i <= j):
            substring = sorted(s2[i:j+1])
            if substring == s1:
                return True
            else:
                i+=1
                j+=1

        return False


        