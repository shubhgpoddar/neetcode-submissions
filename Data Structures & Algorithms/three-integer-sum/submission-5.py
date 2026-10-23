class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]

        nums.sort()

        triplets = []
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                continue

            l = i + 1
            r = len(nums) - 1

            seenl = set()
            seenr = set()

            while l < len(nums) and r >=0 and l < r:
                if nums[l] in seenl:
                    l+=1
                elif nums[r] in seenr:
                    r-=1
                else:
                    target = nums[l] + nums[r] + nums[i]
                    if target > 0:
                        seenr.add(nums[r])
                        r-=1
                        
                    elif target < 0:
                        seenl.add(nums[l])
                        l+=1
                    else:
                        triplets.append([nums[i], nums[l], nums[r]])
                        seenr.add(nums[r])
                        seenl.add(nums[l])
                        l+=1
            seen.add(nums[i])
        return triplets







        