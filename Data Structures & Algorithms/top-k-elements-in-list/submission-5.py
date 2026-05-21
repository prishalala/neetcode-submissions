class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=0
        l=[]
        while True:
            large=0
            if c==k:
                break
            else:
                for i in nums:
                    if i not in l:
                        x=nums.count(i)
                        if x>large:
                            large=x
                            no=i
                l.append(no)
                c+=1
        return l


