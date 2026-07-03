class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.countSolution(s, t)

    def sortingSolution(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def countSolution(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def hashMapSolution(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ds = {}
        dt = {}
        
        for i in s:
            ds[i] = ds.get(i, 0) + 1
            
        for i in t:
            dt[i] = dt.get(i, 0) + 1
            
        return ds == dt