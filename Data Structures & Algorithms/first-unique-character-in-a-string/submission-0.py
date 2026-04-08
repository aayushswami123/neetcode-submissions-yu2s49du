class Solution:
    def firstUniqChar(self, s: str) -> int:
      res = defaultdict(int)
      for c in s:
        res[c] += 1
      for i ,c in enumerate(s):
        if res[c] == 1:
          return i
      return -1 

        