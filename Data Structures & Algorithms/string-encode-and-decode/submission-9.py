class Solution:
    '''
    4:42 - 4:55
    '''

    def encode(self, strs: List[str]) -> str:
        '''
        1. Take each word and prepend with the length.
        2. Join and return as a string
        e.g ["Hello","World"]
        5Hello5World
        e.g [""]
        0
        '''
        res = ""
        for word in strs:
            n = len(word)
            res = res + str(n) + "#" + word
        return res


    def decode(self, s: str) -> List[str]:
        '''
        1. Start with 0th character. Traverse for n length and append to result. Use a while loop, i = 0, increment i and traverse until we get the word. Append to result.
        e.g 5Hello5World
        - "Hello", "World"
        e.g 1
        '''
        res = []
        i = 0
        N = len(s)

        while (i < N):
            wordLength = ""
            while s[i]!="#":
                wordLength+=s[i]
                i+=1
            word = ""
            count = 1
            while count <= int(wordLength):
                word = word + s[i+count]
                count+=1
            res.append(word)
            i+=count
        return res





