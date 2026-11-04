class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        optimized: 8:51
        1. build freq map of abc: freq map of all 26 alphabets
        2. build freq map of substring. if same return
        '''

        freqS1 = defaultdict(int)
        for ch in s1:
            freqS1[ch]+=1
        
        N1 = len(s1)
        N2 = len(s2)
        i = 0

        while (i < N2):
            count = 0
            freqSub = defaultdict(int)
            while (count < N1 and (i+count < N2)):
                freqSub[s2[i+count]]+=1
                count+=1
            if freqSub == freqS1:
                return True
            i+=1
        
        return False



        