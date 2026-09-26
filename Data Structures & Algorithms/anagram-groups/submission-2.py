from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sval = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            sval[sorteds].append(s)
        return list(sval.values())