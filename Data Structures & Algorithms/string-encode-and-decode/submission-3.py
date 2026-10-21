class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""

        for word in strs:
            encodedStr = encodedStr + str(len(word)) + "#" + word
        return encodedStr

    def decode(self, s: str) -> List[str]:
        res = []
        ch = 0
        while (ch < len(s)):
            j = ch
            
            while s[j]!='#':
                j += 1
            wordLength = int(s[ch:j])
            ch = j + 1
            j = ch + wordLength
            word = s[ch:j]
            ch = j
            res.append(word)
        return res


