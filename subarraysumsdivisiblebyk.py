class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        psum = 0
        res = 0
        count = 0
        for i, val in enumerate(nums):
            psum += val
            res += dic[psum % k]
            dic[psum % k] += 1
        return res

        
