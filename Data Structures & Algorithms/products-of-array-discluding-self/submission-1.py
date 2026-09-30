class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        for num in nums:
            product *= num
        for i in range(len(nums)):
            if(nums[i] != 0):
                result.append(product // nums[i])
            else:
                prod_zero = 1
                for j in range(len(nums)):
                    if(i != j):
                        prod_zero *= nums[j]
                result.append(prod_zero)
        return result