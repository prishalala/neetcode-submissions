from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        used = set()
        
        for i in range(len(strs)):
            if i in used:
                continue
                
            group = [strs[i]]
            used.add(i)
            
            for j in range(i + 1, len(strs)):
                if j not in used and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    used.add(j)
            
            result.append(group)
        
        return result