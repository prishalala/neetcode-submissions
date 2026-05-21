class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1=''
        for i in digits:
            str1+=str(i)
        no=int(str1)
        no+=1
        st=str(no)
        l=list(st)
        return l

