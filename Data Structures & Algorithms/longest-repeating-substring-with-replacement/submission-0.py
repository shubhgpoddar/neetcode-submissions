class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        freq = defaultdict()
        L = 0
        maxFrequency = 0

        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R], 0) + 1
            maxFrequency = max(maxFrequency, freq[s[R]])

            if ((R-L+1-maxFrequency) <= k):
                count = max(count, R-L+1)
            else:
                freq[s[L]]-=1
                L+=1
        return count

            


            
                