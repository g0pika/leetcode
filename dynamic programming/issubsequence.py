class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n1 = len(s)
        n2 = len(t)
        if n1 > n2:
            return False
        if n1 == 0:
            return True
        for j in range(n2):
            if t[j] == s[i]:
                i+=1
                if i == n1:
                    return True
                
                    
        
