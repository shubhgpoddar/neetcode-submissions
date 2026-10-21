class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "#"
        delimiter = ";"
        output = []

        for word in strs:
            encodedStr = ";".join(str(ord(ch)) for ch in word)
            output.append(encodedStr)
        
        res = "+".join(output)
        return res

    def decode(self, s: str) -> List[str]:
        if s == "#":
            return []

        words = s.split("+")

        output = []
        for word in words:
            if word == "":
                output.append(word)
            else:
                decodedList = word.split(";")
                decoded = "".join(chr(int(char)) for char in decodedList)
                output.append(decoded)

        return output

