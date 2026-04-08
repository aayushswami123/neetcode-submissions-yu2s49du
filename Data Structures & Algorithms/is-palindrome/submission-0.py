class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join(c for c in s if c.isalnum()).lower()
        if new_str == new_str[::-1]:
            return True
        else:
            return False
        

        