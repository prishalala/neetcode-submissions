class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        else:
            l=list(s)
            for i in range(len(l)):
                temp=l.pop(i)
                if l==l[::-1]:
                    return True
                l.insert(i,temp)
        

        return False