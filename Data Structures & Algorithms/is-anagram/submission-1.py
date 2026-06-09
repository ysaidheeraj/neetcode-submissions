from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable = [0] * 26
        s.lower()
        t.lower()
        for c in s:
            hashtable[ord(c) - ord('a')] += 1
        
        for c in t:
            hashtable[ord(c) - ord('a')] -= 1
        
        for char in hashtable:
            if char != 0:
                return False
        
        return True
