class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefixProduct = [1]
        for i in range(1, len(nums)):
            product = nums[i-1] * prefixProduct[i-1]
            prefixProduct.append(product)
        
        suffixProduct = [0] * len(nums)
        suffixProduct[len(nums)-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffixProduct[i] = nums[i + 1] * suffixProduct[i + 1]

        res = []
        for i in range(len(nums)):
            res.append(prefixProduct[i] * suffixProduct[i])
        return res
