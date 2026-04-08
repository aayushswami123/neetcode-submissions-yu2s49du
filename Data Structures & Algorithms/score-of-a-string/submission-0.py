class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0 
        for i in range(len(s)-1):
            diff = abs(ord(s[i+1])- ord(s[i]))
            score += diff
        return score