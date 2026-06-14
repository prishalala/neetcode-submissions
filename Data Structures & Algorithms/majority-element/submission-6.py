from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        large=0
        frequency=Counter(nums)
        for i in nums:
            
            if frequency[i]>(len(nums)/2):
                if frequency[i]>large:
                    large=frequency[i]
                    no=i
        return no