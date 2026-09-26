class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                continue
        if len(seen) != len(nums):
            return True
        else:
            return False