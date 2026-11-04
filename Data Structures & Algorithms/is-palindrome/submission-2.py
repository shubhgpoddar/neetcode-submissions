class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        4:53
        case insensitive => convert to lowercase()
        Use 2 pointers: if no alpha numeric characters: dont compare, move THAT specific   pointer
        '''

        i = 0
        N = len(s)
        j = N - 1

        while(i < N and j >= 0 and i <= j):
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True

        