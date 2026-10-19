class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch) - ord('a')] = count[ord(ch) - ord('a')] + 1
            if tuple(count) in res:
                res[tuple(count)].append(word)
            else:
                res[tuple(count)] = [word]
        
        return list(res.values())

        