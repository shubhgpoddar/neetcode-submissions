from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1 = defaultdict(int)

        for ch in s1:
            freqs1[ch] += 1

        have = 0
        need = len(freqs1)
        freqs2 = defaultdict(int)
        L = 0

        for R in range(len(s2)):
            ch = s2[R]
            freqs2[ch] += 1

            if ch in freqs1 and freqs2[ch] == freqs1[ch]:
                have += 1
            elif ch in freqs1 and freqs2[ch] == freqs1[ch] + 1:
                have -= 1

            while R - L + 1 > len(s1):
                left = s2[L]
                if left in freqs1 and freqs2[left] == freqs1[left]:
                    have -= 1
                freqs2[left] -= 1
                if left in freqs1 and freqs2[left] == freqs1[left]:
                    have += 1
                L += 1

            if R - L + 1 == len(s1) and have == need:
                return True

        return False