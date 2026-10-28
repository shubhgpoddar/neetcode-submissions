
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = defaultdict(int)  # CHANGED: initialize missing keys to 0
        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1

        res = ""  # CHANGED: return "" if no valid window exists
        freqSubstring = defaultdict(int)  # CHANGED: initialize missing keys to 0
        L = 0
        formed = 0  # CHANGED: number of characters meeting required frequency
        required = len(freqT)  # CHANGED: number of distinct required characters

        for R in range(len(s)):
            # CHANGED: add the right character before checking the window
            if s[R] in freqT:
                freqSubstring[s[R]] += 1
                if freqSubstring[s[R]] == freqT[s[R]]:
                    formed += 1

            # CHANGED: shrink repeatedly while the window is valid
            while formed == required:
                curr = s[L:R+1]
                if not res or len(curr) < len(res):
                    res = curr

                # CHANGED: only remove the character leaving from the left
                if s[L] in freqT:
                    freqSubstring[s[L]] -= 1
                    if freqSubstring[s[L]] < freqT[s[L]]:
                        formed -= 1
                L += 1

        return res
