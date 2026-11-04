class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        order doesnt matter => frequency map
        Time: O(n + m)
        Space(O(1)) -> at most 26
        '''

        fs = defaultdict(int) # at most 26
        for ch in s:
            fs[ch]+=1
        ft = defaultdict(int) # at most 26
        for ch in t: 
            ft[ch]+=1
        return fs==ft



        