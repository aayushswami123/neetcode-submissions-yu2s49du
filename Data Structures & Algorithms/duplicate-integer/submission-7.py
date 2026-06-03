class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasha = set()
        for num in nums:
            if num not in hasha:
                hasha.add(num)
        if len(hasha) != len(nums):
            return True
        else:
            return False
            
