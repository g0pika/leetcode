class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank[0])
        
        out = 0
        prev = ''
        for b in filter(lambda x: x!='0'*n, bank):
            if prev:
                out += b.count('1')*prev.count('1')
            prev = b
        
        return out
