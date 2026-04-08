class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     hash = {}
     for i,n in enumerate(nums):
        print(i,n)
        comp = target - n
        if comp in hash :
            return [hash[comp], i ]
        hash[n] = i


      
