class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in res:
                res[sortedWord].append(word)
            else:
                res[sortedWord] = [word]
        return list(res.values())
        