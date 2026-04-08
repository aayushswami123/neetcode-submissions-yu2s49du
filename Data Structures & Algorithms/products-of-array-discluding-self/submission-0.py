class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]* len(nums)
        prefix_sum = 1
        for i in range(len(nums)):
            res[i] = prefix_sum
            prefix_sum *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *=postfix
            postfix *=nums[i]
        return res




        
            