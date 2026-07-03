class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.countSolution(s, t)

    def sortingSolution(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def countSolution(self, s: str, t: str) -> bool:
        cs = Counter(s)
        ct = Counter(t)
        return cs == ct

        