class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        11:58 12:07
        Algorithm:
        1. Create a dictionary with frequency tuple as key and string as values.
        2. Iterate through each word and check if the frequency tuple in dictionary, else create and assign word
        3. Return dictionary values.

        # ["act","pots","tops","cat","stop","hat"]
        {(a c t): [act, cat], (t o p s): [tops, stop], (hat): [hat]}
        Time: O(nmlogm)

        wordMap = defaultdict(list)

        for word in strs: # O(n)
            freq = []
            for ch in word: # O(m)
                freq.append(ch)
            freq.sort() # O mlogm
            key = tuple(freq)
            wordMap[key].append(word)
        
        return list(wordMap.values())

        12:11 - 


        '''

        wordMap = defaultdict(list)

        for word in strs: # O(n)
            freq = [0]*26
            for ch in word:
                index = ord(ch) - ord('a')
                freq[index]+=1
            key = tuple(freq)
            wordMap[key].append(word)
        
        return list(wordMap.values())



        