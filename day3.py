class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
	    return not len(Counter(ransomNote) - Counter(magazine))
