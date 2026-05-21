from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            if len(stones) == 2:
                return abs(stones[0] - stones[1])
            
            c = max(stones)
            stones.remove(c)
            d = max(stones)
            stones.remove(d)
            
            if c != d:
                stones.append(abs(c - d))
        
        return stones[0] if stones else 0