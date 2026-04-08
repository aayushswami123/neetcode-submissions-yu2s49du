class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtab = {}
        for i , n in enumerate(nums):
            comp = target - n
            if comp in hashtab:
                return [hashtab[comp], i]
            hashtab[n] = i