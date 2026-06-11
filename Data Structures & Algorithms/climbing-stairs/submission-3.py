class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            l=[1,2]
            for i in range(3,n+1):
                l.append((l[i-2]+l[i-3]))
            return l[-1]