class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = defaultdict()
        freqS = defaultdict()

        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1
            freqS[ch] = 0

        have = 0
        need = len(freqT.keys())
        res = ""
        resLen = float("infinity")
        L = 0

        for R in range(len(s)):
            ch = s[R]
            if ch in freqS:
                freqS[ch]+=1
                if freqS[ch] == freqT[ch]:
                    have+=1
                
            while have == need:
                # update result length
                if (R-L+1) < resLen:
                    res = s[L:R+1]
                    resLen = R-L+1
                # update L to find smallest string
                if s[L] in freqS:
                    freqS[s[L]]-=1
                    if freqS[s[L]] < freqT[s[L]]:
                        have-=1
                L+=1
        
        return res if resLen!=float("infinity") else ""






        

        