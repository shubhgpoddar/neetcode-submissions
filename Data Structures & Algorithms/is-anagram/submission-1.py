class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyS = defaultdict()
        for ch in s:
            frequencyS[ch] = 1 + frequencyS.get(ch, 0)
        frequencyT = defaultdict()
        for ch in t:
            frequencyT[ch] = 1 + frequencyT.get(ch, 0)
        return frequencyT==frequencyS
        

        