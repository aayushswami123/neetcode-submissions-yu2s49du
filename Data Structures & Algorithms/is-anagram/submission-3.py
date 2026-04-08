class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasha = {}
        hashb = {}
        for char in s :
            hasha[char] = hasha.get(char,0) + 1
        for char in t :
            hashb[char] = hashb.get(char,0) + 1
        if hasha != hashb:
            return False
        else:
            return True