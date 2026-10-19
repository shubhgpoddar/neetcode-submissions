class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        r = 0
        currentSubstring = set()

        while (l < len(s) and r < len(s) and r >= l):
            while(s[r] in currentSubstring):
                currentSubstring.remove(s[l])
                l+=1
            currentSubstring.add(s[r])
            longest = max(longest, len(currentSubstring))
            r+=1
        
        return longest   
            

