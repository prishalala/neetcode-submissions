class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        word3=''
        if l1>l2:
            for i in range(l2):
                word3 += word1[i] + word2[i]
            for i in range(l2,l1):
                word3 += word1[i]
        elif l2>l1:
            for i in range(l1):
                word3+=word1[i]+word2[i]
            for i in range(l1,l2):
                word3+=word2[i]
        else:
            for i in range(l1):
                word3+=word1[i]+word2[i]
        return word3