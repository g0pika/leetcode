

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ls = []
        sm = 0
        mul = 0
        rows = len(bank)
        cols = len(bank[0])
        
        for i in range(0, rows):
            sumrow = 0
            for j in range(0, cols):
                sumrow += int(bank[i][j])
            if sumrow != 0:
                ls.append(sumrow)    
            
        
        for i in range(len(ls)-1):
            mul = ls[i] * ls[i+1]
            sm += mul
        return sm
            
