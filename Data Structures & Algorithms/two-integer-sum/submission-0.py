class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in hashmap:
                return [hashmap[compl],i]
            hashmap[nums[i]] = i
            
            