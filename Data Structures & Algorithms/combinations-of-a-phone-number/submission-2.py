class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar={
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",
        }
        temp=[""]
        for i in digits:
            l=[]
            for j in temp:
                for k in digitToChar[i]:
                    l.append(j+k)
            temp=l
        
        return temp