class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]
        while True:
            c = self.sos(n)
            if c == 1:
                return True
            if c not in l:
                l.append(c)
                n = c
            else:
                return False



    def sos(self,n):
        sum=0
        while n>0:
            r=n%10
            sum+=r*r
            n=n//10
        return sum