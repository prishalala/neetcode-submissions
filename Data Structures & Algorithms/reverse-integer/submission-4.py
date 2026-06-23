class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            num=abs(x)
            st=str(num)
            rev=st[::-1]
            num=(-1)*int(rev)
            if -2**31<=num<=2**31-1:
                return num
            else:
                return 0
        

        st=str(x)
        rev=st[::-1]
        num=int(rev)
        if -2**31<=num<=(2**31)-1:
            return num
        else:
            return 0