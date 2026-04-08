class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        ans = 0
        for n in sett:
            if (n-1) not in sett:
                leng = 0
                while (n+leng) in sett:
                    leng+=1
                ans = max(leng, ans)
        return ans

