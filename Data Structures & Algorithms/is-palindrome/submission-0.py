class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = []

        for ch in s:
            if ch.isalnum():
                forward.append(ch.lower())
        

        reverse = []
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                reverse.append(s[i].lower())

        return ''.join(forward) == ''.join(reverse)