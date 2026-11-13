class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        5:33
        j moves until condition is unsatisfied
        i moves until condition is unsatisfied
        '''

        freqT = defaultdict(int)
        for ch in t:
            freqT[ch]+=1
        have = 0
        need = len(freqT.keys())
        
        res = ""
        resLength = len(s)
        N = len(s)
        i = 0
        j = 0

        freqS = defaultdict(int)
        

        while i < N and j < N and i <=j:
            if s[j] in t:
                freqS[s[j]]+=1
                if freqS[s[j]] == freqT[s[j]]:
                    have+=1
            while have == need:
                if resLength >= j-i+1:
                    resLength = j-i+1
                    res = s[i:j+1]
                if s[i] in t:
                    freqS[s[i]]-=1
                    if freqS[s[i]] < freqT[s[i]]:
                        have-=1
                i+=1
            j+=1


        return res

            


        

        
        