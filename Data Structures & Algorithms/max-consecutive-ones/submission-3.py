class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c1=0
        l=[]
        for i in nums:
            if i==1:
                c1+=1
            else:
                l.append(c1)
                c1=0
        l.append(c1)
        return max(l)
