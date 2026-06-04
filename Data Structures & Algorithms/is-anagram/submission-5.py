class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasha = Counter(s)
        hashb = Counter(t)
        if hasha != hashb:
            return False
        else:
            return True

