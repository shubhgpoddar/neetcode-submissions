class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        order doesnt matter => frequency map
        '''

        fs = defaultdict(int)
        for ch in s:
            fs[ch]+=1
        ft = defaultdict(int)
        for ch in t:
            ft[ch]+=1
        return fs==ft



        