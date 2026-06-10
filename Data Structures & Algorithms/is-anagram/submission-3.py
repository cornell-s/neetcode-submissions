class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        lettersT = collections.Counter(t)
        lettersS = collections.Counter(s)

        if(lettersT != lettersS):
            return False

        return True   