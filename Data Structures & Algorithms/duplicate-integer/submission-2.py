class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_num = len(set(nums))
        if set_num == len(nums):
            return False
        else:
            return True
        