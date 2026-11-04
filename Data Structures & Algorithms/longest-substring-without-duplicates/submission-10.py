class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        8:08 - 8:31
        Algorithm:
        i and j
        max:
        increment j until the substring is unique -> if ch in seen:
         - compare current with the running sequence
        increment i, remove ch until the substring becomes unique
        a) zxyyxyzabbc
        0,3 seen = y y
        3 3
        '''
        res = 0
        N = len(s)
        i = 0
        j = i

        seen = set()
        while(i < N and j < N and i <= j):
            if s[j] not in seen:
                substring = s[i:j+1]
                res = max(res, len(substring))
                seen.add(s[j])
                j+=1
            else:
                # got stuck here in the while loop - no hints
                while(s[j] in seen):
                    seen.remove(s[i])
                    i+=1
        return res        



            

        
        