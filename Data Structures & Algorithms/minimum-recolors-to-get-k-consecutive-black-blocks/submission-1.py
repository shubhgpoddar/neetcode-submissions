class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = len(blocks)
        L = 0
        R = 0
        window = 1

        freq = defaultdict()

        while R < len(blocks) and window <= k:
            freq[blocks[R]] = freq.get(blocks[R], 0) + 1
            window = R - L + 1

            if window == k:
                count = min(count, freq.get('W', 0))
                freq[blocks[L]]-=1
                L+=1
            R+=1
        return count



        