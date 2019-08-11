from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.getCombos(res, candidates, [], 0, target)
        return res

    def getCombos(self, res, cs, combo: List[List[int]], idx, target):
        if target == 0:
            res.append(combo)
            return

        for i in range(idx, len(cs)):
            if cs[i] > target:
                break
            if i > idx and cs[i] == cs[i-1]:
                continue
            self.getCombos(res, cs, combo+[cs[i]], i+1, target-cs[i])



print(Solution().combinationSum2(candidates = [2,5,2,1,2]
, target = 5))
