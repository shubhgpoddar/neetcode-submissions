class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. Use a set and compare lengths()
        # 2. use a seen set. If value in seen, return false

        seen = set()
        N = len(nums)
        for i in range(N):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False

        