class Solution:
    def countone(self,n):
        count=0
        while (n!=0):
            if n%2!=0:
                count+=1
            n=n//2
        return count
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1):
            l.append(self.countone(i))
        return l