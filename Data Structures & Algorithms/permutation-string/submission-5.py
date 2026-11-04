import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        more optimized
        9:11 
        '''
        freqS1 = dict.fromkeys(string.ascii_lowercase, 0)
        for ch in s1:
            freqS1[ch]+=1
        
        N1 = len(s1)
        N2 = len(s2)
        i = 0
        j = i

        freqS2 = dict.fromkeys(string.ascii_lowercase, 0)

        while(i < N2):
            while j < N2 and i <= j and j-i != N1:
                freqS2[s2[j]]+=1
                j+=1
            print("RESULT", freqS2)
            if freqS2 == freqS1:
                return True
            freqS2[s2[i]]-=1
            i+=1
        return False
            

        